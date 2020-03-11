# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 23:11:45 2020

@author: Dan
"""


from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from Libraries.HR import HR
from Libraries.Data import Data

data_array = np.genfromtxt('data/data_01_075.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())

fs = int(data.calc_sampling_rate()) #sampling rate in Hz
t = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s = data_array[:,4] #get the x-acceleration array
s = HR.detrend(s,fs)



filter_order = 3
filter_cutoff = 5
b,a = signal.butter(filter_order, filter_cutoff, btype='lowpass')


s_filt = signal.lfilter(b,a,s)


w, h = signal.freqz(b,a)

# plt.plot(w, 20 * np.log10(abs(h)))
# plt.show()

fig = plt.gcf()
fig.set_size_inches(10, 6)
plt.clf()
plt.subplot(311)
plt.plot(w, 20 * np.log10(abs(h)))
plt.title("filter resp")
plt.subplot(334)
plt.plot(s)
plt.subplot(335)
Pxx,Freqs = plt.psd(s, NFFT=len(t), Fs=fs)
plt.subplot(337)
plt.plot(s_filt)
plt.subplot(338)
Pxx2, Freqs2 = plt.psd(s_filt, NFFT=len(t), Fs=fs)
plt.subplot(336)
plt.plot(Freqs,Pxx)
plt.subplot(339)
plt.plot(Freqs2,Pxx2)




# plt.clf()
# plt.plot(s)
# plt.show()

# plt.clf()
# plt.psd(s, NFFT=len(t), Fs=fs)
# plt.show()

# Pxx, Freqs = plt.psd(s, NFFT=len(t), Fs=fs)
# print(Freqs[np.argmax(Pxx)])


# plt.clf()
# plt.plot(Freqs, Pxx)
# plt.show()



# [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(s,fs)
# print("BPM = "+str(BPM_Estimate))











































