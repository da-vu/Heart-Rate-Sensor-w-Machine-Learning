# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 18:27:06 2020

@author: Dan
"""

import matplotlib.pyplot as plt
import numpy as np

class HR:
    
    def calc_heart_rate_time(s,fs):
        s_diff = HR.signal_diff(-s) #preprocess the signal, I chose to use diff
        norm_s_diff = HR.normalize_signal(s_diff) #normalize the signal
        threshold = 0.7 #empirically determined to be a good threshold
        s_thresh = [int(val > threshold) for val in norm_s_diff] #threshold the normalized signal. convert to int from boolean in order to perform logic of up or down transition
        s_thresh_up = HR.signal_diff(s_thresh) > 0 #check for up transition (start of heart beat)
        BPM = np.sum(s_thresh_up)/((len(s_thresh_up)+1)/fs/60) #count the number of heart beats and divide by the total time. Total time is calculated as the length of the measurement (samples) / fs (samples/s) / 60 (min/s). This gives us beats/min
        return BPM, s_thresh_up
    
    def normalize_signal(s):
        norm_signal = (s - np.min(s))/(np.max(s)-np.min(s))
        return norm_signal

    def moving_average(s,n_avg):
        ma = np.zeros(s.size)
        for i in np.arange(0,len(s)):
          ma[i] = np.mean(s[i:i+n_avg])
        return ma
    
    
    def detrend(s,n_avg): #remove the moving average from the signal
        ma = HR.moving_average(s,n_avg)
        return s - ma
    
    def signal_diff(s):
        s_diff = np.diff(s,1,0)
        s_diff = np.append(s_diff, 0) #np.diff returns one shorter, so need to add a 0
        return s_diff
