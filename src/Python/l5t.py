# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:47:05 2020

@author: Dan
"""


import numpy as np
import matplotlib.pyplot as plt
from Libraries.HR import HR
from Libraries.Data import Data

data_array = np.genfromtxt('data/appendix_a.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())

fs = int(data.calc_sampling_rate()) #sampling rate in Hz
t = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s = data_array[:,4] #get the x-acceleration array
s = HR.detrend(s,fs)




plt.clf()
plt.subplot(211)
plt.plot(t, s)
plt.subplot(212)
plt.psd(s, NFFT=len(t), Fs=fs) #plot the power spectral density
plt.show()


Pxx, Freqs = plt.psd(s, NFFT=len(t), Fs=fs)


while np.argmax(Pxx) == 0:
    Pxx = np.delete(Pxx, 0)
    Freqs = np.delete(Freqs, 0)

print(Freqs[np.argmax(Pxx)])


plt.clf()
plt.plot(Freqs, Pxx)
plt.show()