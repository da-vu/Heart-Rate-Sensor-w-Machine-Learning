# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:25:33 2020

@author: Dan
"""

import matplotlib.pyplot as plt
import numpy as np


def calc_heart_rate_time(signal,fs):
    #filter the signal to remove baseline drifting
    signal = remove_offset(signal)
    plotSig(signal)
    #filter the signal to remove high frequency noise
    signal = moving_average(signal,10)
    plotSig(signal)
    #Normalize the signal between 0 and 1
    signal = normalize_signal(signal)
    plotSig(signal)
    #Explore using the signal directly or potentially using the diff of the signal. 
    signal = signal_diff(signal)
    plotSig(signal)
    #Count the number of times the signal crosses a threshold.
    threshold = -0.01
    count = 0
    for i in range(len(signal)):
        if signal[i] <threshold and signal[i+1] >threshold:
            count = count+1
    print(count)
    #Calculate the beats per minute. 
    beats = count * 6
    print(beats)

def normalize_signal(signal):
    #find min of signal
    norm_signal = signal
    minval = np.amin(norm_signal)
    print(minval)
    #subtract the minimum so the minimum of the signal is zero
    norm_signal = norm_signal-minval
    #find the new maximum of the signal
    maxval = np.amax(norm_signal)
    print(maxval)
    #divide the signal by the new maximum so the maximum becomes 1
    norm_signal = norm_signal/maxval
    return norm_signal


def remove_offset(signal):
    s = signal 
    mean_s = np.average(s)
    s = s-mean_s
    # plt.clf()
    # plt.plot(s)
    # plt.show()
    return s

def detrend(s,n_avg): #remove the moving average from the signal
    ma = moving_average(s,n_avg)
    return s-ma #s minus the moving_average

def moving_average(s,n_avg):
    ma = np.zeros(s.size) 
    for i in np.arange(0,len(s)):
      ma[i] =  np.average(s[i:i+n_avg])   #mean of s from index i to i+n_avg
    return ma

def signal_diff(s):
    s_diff = np.diff(s) #calculate the gradient using np.diff
    s_diff = np.append(s_diff, 0) #np.diff returns one shorter, so need to add a 0
    return s_diff

def plotSig(signal):
    plt.clf()
    plt.plot(signal)
    plt.show()
    
def plotData(data_array):
    time = data_array_saved[:,0]
    plt.clf()
    plt.subplot(411)
    
    plt.title("Example Data Plot")
    
    plt.plot(time,data_array[:,1])
    
    plt.ylabel("X Amplitude")
    
    plt.subplot(412)
    plt.plot(time,data_array[:,2])
    plt.ylabel("Y Amplitude")
    
    plt.subplot(413)
    plt.plot(time,data_array[:,3])
    plt.ylabel("Z Amplitude")
    
    plt.subplot(414)
    plt.plot(time,-data_array[:,4])
    
    plt.xlabel(u'Time(${\mu}s$)')
    plt.ylabel("R Amplitude")
    
    # plt.tight_layout() 
    plt.show()

if __name__== "__main__":
    
    data_array_saved = np.genfromtxt('data_04_128.csv', delimiter=',') 
    plotData(data_array_saved)
    
    signal = data_array_saved[:,4]
    calc_heart_rate_time(signal, 50)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
