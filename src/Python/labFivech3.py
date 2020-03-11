# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 18:13:05 2020

@author: Dan
"""


from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
from Libraries.HR import HR
from Libraries.Data import Data
from matplotlib.pyplot import figure
from Libraries.Visualize import Visualize
import os
import glob

esti=[]
reff=[]
all_files = [os.path.basename(x) for x in glob.glob('data/data*.csv')]
for file in all_files:
    # if len(file)==15:
    temp=file[8:11]
    temp=float(temp)
    print(temp)
    reff.append(temp)



data_array = np.genfromtxt('data/data_01_075.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())
fs = int(data.calc_sampling_rate()) #sampling rate in Hz
t = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s = data_array[:,4] 
esti.append(HR.calc_heart_rate_freq(s, fs))
# s = HR.preprocess(-s,fs)
# Pxx, Freqs = plt.psd(s, NFFT=len(t), Fs=fs)
# while np.argmax(Pxx) == 0:
#     Pxx = np.delete(Pxx, 0)
#     Freqs = np.delete(Freqs, 0)
# esti.append(Freqs[np.argmax(Pxx)]*60)
# print(Freqs[np.argmax(Pxx)])
plt.clf()

data_array = np.genfromtxt('data/data_02_074.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())
fs1 = int(data.calc_sampling_rate()) #sampling rate in Hz
t1 = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s1 = data_array[:,4]
esti.append(HR.calc_heart_rate_freq(s1, fs1)) 
# s1 = HR.preprocess(-s1,fs1)
# Pxx1, Freqs1 = plt.psd(s1, NFFT=len(t1), Fs=fs1)
# while np.argmax(Pxx1) == 0:
#     Pxx1 = np.delete(Pxx1, 0)
#     Freqs1 = np.delete(Freqs1, 0)
# esti.append(Freqs[np.argmax(Pxx1)])
# print(Freqs1[np.argmax(Pxx1)])
plt.clf()

data_array = np.genfromtxt('data/data_03_077.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())
fs2 = int(data.calc_sampling_rate()) #sampling rate in Hz
t2 = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s2 = data_array[:,4] 
esti.append(HR.calc_heart_rate_freq(s2, fs2))
# s2 = HR.preprocess(-s2,fs2)
# Pxx2, Freqs2 = plt.psd(s2, NFFT=len(t2), Fs=fs2)
# while np.argmax(Pxx2) == 0:
#     Pxx2 = np.delete(Pxx2, 0)
#     Freqs2 = np.delete(Freqs2, 0)
# print(Freqs2[np.argmax(Pxx2)])
# esti.append(Freqs[np.argmax(Pxx2)])
plt.clf()

data_array = np.genfromtxt('data/data_04_128.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())
fs3 = int(data.calc_sampling_rate()) #sampling rate in Hz
t3 = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s3 = data_array[:,4] 
esti.append(HR.calc_heart_rate_freq(s3, fs3))
# s3 = HR.preprocess(-s3,fs3)
# Pxx3, Freqs3 = plt.psd(s3, NFFT=len(t3), Fs=fs3)
# while np.argmax(Pxx3) == 0:
#     Pxx3 = np.delete(Pxx3, 0)
#     Freqs3 = np.delete(Freqs3, 0)
# print(Freqs3[np.argmax(Pxx3)])
# esti.append(Freqs[np.argmax(Pxx3)])
plt.clf()

data_array = np.genfromtxt('data/data_05_086.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())
fs4 = int(data.calc_sampling_rate()) #sampling rate in Hz
t4 = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s4 = data_array[:,4] 
esti.append(HR.calc_heart_rate_freq(s4, fs4))
# s4 = HR.preprocess(-s4,fs4)
# Pxx4, Freqs4 = plt.psd(s4, NFFT=len(t4), Fs=fs4)
# while np.argmax(Pxx4) == 0:
#     Pxx4 = np.delete(Pxx4, 0)
#     Freqs4 = np.delete(Freqs4, 0)
# print(Freqs4[np.argmax(Pxx4)])
# esti.append(Freqs[np.argmax(Pxx4)])
plt.clf()

data_array = np.genfromtxt('data/data_06_077.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())
fs5 = int(data.calc_sampling_rate()) #sampling rate in Hz
t5 = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s5 = data_array[:,4] 
esti.append(HR.calc_heart_rate_freq(s5, fs5))
# s5 = HR.preprocess(-s5,fs5)
# Pxx5, Freqs5 = plt.psd(s5, NFFT=len(t5), Fs=fs5)
# while np.argmax(Pxx5) == 0:
#     Pxx5 = np.delete(Pxx5, 0)
#     Freqs5 = np.delete(Freqs5, 0)
# print(Freqs5[np.argmax(Pxx5)])
# esti.append(Freqs[np.argmax(Pxx5)])
plt.clf()

data_array = np.genfromtxt('data/data_07_080.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())
fs6 = int(data.calc_sampling_rate()) #sampling rate in Hz
t6 = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s6 = data_array[:,4] 
esti.append(HR.calc_heart_rate_freq(s6, fs6))
# s6 = HR.preprocess(s6,fs6)
# Pxx6, Freqs6 = plt.psd(-s6, NFFT=len(t6), Fs=fs6)
# while np.argmax(Pxx6) == 0:
#     Pxx6 = np.delete(Pxx6, 0)
#     Freqs6 = np.delete(Freqs6, 0)
# print(Freqs6[np.argmax(Pxx6)])
# esti.append(Freqs[np.argmax(Pxx6)])
plt.clf()

data_array = np.genfromtxt('data/data_08_085.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())
fs7 = int(data.calc_sampling_rate()) #sampling rate in Hz
t7 = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s7 = data_array[:,4] 
esti.append(HR.calc_heart_rate_freq(s7, fs7))
# s7 = HR.preprocess(s7,fs7)
# Pxx7, Freqs7 = plt.psd(-s7, NFFT=len(t7), Fs=fs7)
# while np.argmax(Pxx7) == 0:
#     Pxx7 = np.delete(Pxx7, 0)
#     Freqs7 = np.delete(Freqs7, 0)
# print(Freqs7[np.argmax(Pxx7)])
# esti.append(Freqs[np.argmax(Pxx7)])
plt.clf()

data_array = np.genfromtxt('data/data_09_080.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())
fs8 = int(data.calc_sampling_rate()) #sampling rate in Hz
t8 = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s8 = data_array[:,4] 
esti.append(HR.calc_heart_rate_freq(s8, fs8))
# s8 = HR.preprocess(s8,fs8)
# Pxx8, Freqs8 = plt.psd(-s8, NFFT=len(t8), Fs=fs8)
# while np.argmax(Pxx8) == 0:
#     Pxx8= np.delete(Pxx8, 0)
#     Freqs8 = np.delete(Freqs8, 0)
# print(Freqs8[np.argmax(Pxx8)])
# esti.append(Freqs[np.argmax(Pxx8)])
plt.clf()

data_array = np.genfromtxt('data/data_10_083.csv', delimiter=',')#get data from Appendix A and save as .csv.
data = Data()
data.add_data(data_array)
print(data.get_num_samples())
fs9 = int(data.calc_sampling_rate()) #sampling rate in Hz
t9 = (data_array[:,0] - data_array[0,0])/1e6#get the time array
s9 = data_array[:,4] 
esti.append(HR.calc_heart_rate_freq(s9, fs9))
# s9 = HR.preprocess(s9,fs9)
# Pxx9, Freqs9 = plt.psd(-s9, NFFT=len(t9), Fs=fs9)
# while np.argmax(Pxx9) == 0:
#     Pxx9 = np.delete(Pxx9, 0)
#     Freqs9 = np.delete(Freqs9, 0)
# print(Freqs9[np.argmax(Pxx9)])
# esti.append(Freqs[np.argmax(Pxx9)])
plt.clf()

esti_arr=np.array(esti)

# =============================================================================
# plt.clf()
# plt.plot(s)
# plt.show()
# 
# 
# plt.clf()
# plt.psd(s, NFFT=len(t), Fs=fs)
# plt.show()
# 
# Pxx, Freqs = plt.psd(s, NFFT=len(t), Fs=fs)
# print(Freqs[np.argmax(Pxx)])
# plt.clf()
# plt.plot(Freqs, Pxx)
# plt.show()
# =============================================================================


# fig, axs = plt.subplots(10, 3, sharex=False, sharey=False)
# fig = plt.gcf()
# fig.set_size_inches(25, 55)

# axs[0, 0].plot(s)
# axs[0, 1].psd(s, NFFT=len(t), Fs=fs)
# axs[0, 2].plot(Freqs, Pxx)


# axs[1, 0].plot(s1)
# axs[1, 1].psd(s1, NFFT=len(t1), Fs=fs1)
# axs[1, 2].plot(Freqs1, Pxx1)


# axs[2, 0].plot(s2)
# axs[2, 1].psd(s2, NFFT=len(t2), Fs=fs2)
# axs[2, 2].plot(Freqs2, Pxx2)

# axs[3, 0].plot(s3)
# axs[3, 1].psd(s3, NFFT=len(t3), Fs=fs3)
# axs[3, 2].plot(Freqs3, Pxx3)

# axs[4, 0].plot(s4)
# axs[4, 1].psd(s4, NFFT=len(t4), Fs=fs4)
# axs[4, 2].plot(Freqs4, Pxx4)

# axs[5, 0].plot(s5)
# axs[5, 1].psd(s5, NFFT=len(t5), Fs=fs5)
# axs[5, 2].plot(Freqs5, Pxx5)

# axs[6, 0].plot(s6)
# axs[6, 1].psd(s6, NFFT=len(t6), Fs=fs6)
# axs[6, 2].plot(Freqs6, Pxx6)

# axs[7, 0].plot(s7)
# axs[7, 1].psd(s7, NFFT=len(t7), Fs=fs7)
# axs[7, 2].plot(Freqs7, Pxx7)

# axs[8, 0].plot(s8)
# axs[8, 1].psd(s8, NFFT=len(t8), Fs=fs8)
# axs[8, 2].plot(Freqs8, Pxx8)

# axs[9, 0].plot(s9)
# axs[9, 1].psd(s9, NFFT=len(t9), Fs=fs9)
# axs[9, 2].plot(Freqs9, Pxx9)

# for ax in axs[:,0]:
#     ax.set_title('Time Domain')
#     ax.set(xlabel='Time($s$)', ylabel='Absorbance')
    
# for ax in axs[:,2]:
#     ax.set_title('Frequency Domain - Fourier Transformed')
#     ax.set(xlabel='Frequency($Hz$)', ylabel='Amplitude')
    
    
# axs[0,1].set_title('Dominant Frequency($Hz$)= ' + str(Freqs[np.argmax(Pxx)]))
# axs[1,1].set_title('Dominant Frequency($Hz$)= ' + str(Freqs1[np.argmax(Pxx1)]))
# axs[2,1].set_title('Dominant Frequency($Hz$)= ' + str(Freqs2[np.argmax(Pxx2)]))
# axs[3,1].set_title('Dominant Frequency($Hz$)= ' + str(Freqs3[np.argmax(Pxx3)]))
# axs[4,1].set_title('Dominant Frequency($Hz$)= ' + str(Freqs4[np.argmax(Pxx4)]))
# axs[5,1].set_title('Dominant Frequency($Hz$)= ' + str(Freqs5[np.argmax(Pxx5)]))
# axs[6,1].set_title('Dominant Frequency($Hz$)= ' + str(Freqs6[np.argmax(Pxx6)]))
# axs[7,1].set_title('Dominant Frequency($Hz$)= ' + str(Freqs7[np.argmax(Pxx7)]))
# axs[8,1].set_title('Dominant Frequency($Hz$)= ' + str(Freqs8[np.argmax(Pxx8)]))
# axs[9,1].set_title('Dominant Frequency($Hz$)= ' + str(Freqs9[np.argmax(Pxx9)]))
# plt.show()

reff_arr=np.reshape(reff,(len(reff),1))
esti_arr=np.reshape(esti,(len(esti),1))
   
print(reff_arr)
print(esti_arr)

arrr = np.hstack((reff_arr,esti_arr))
arrr = np.reshape(arrr,(10,2))
print(arrr)


Visualize.plotBandAltmann(arrr)