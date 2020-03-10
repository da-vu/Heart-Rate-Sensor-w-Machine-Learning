# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 21:38:02 2020

@author: Dan
"""



import glob
import os
#from Libraries.Connection import Connection
#from Libraries.Visualize import Visualize
from Libraries.HR import HR
from Libraries.Data import Data
import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture as GMM
import time
start_time = time.time()


unique_ids = []

all_files = [os.path.basename(x) for x in glob.glob('data/data/training/*.csv')]#the correct regex)
# print(all_files)#check what is in your all_files by printing. You should get a list of strings of the filenames.


for file in all_files:
    sub_id = file[:2]
    if sub_id not in unique_ids:
        unique_ids.append(sub_id)
print(unique_ids)
    


list_data = []
list_sub = []
list_ref = []
list_trials = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']


for sub_id in unique_ids:#sub_id in the list of unique_ids
    sub_files = [os.path.basename(x) for x in glob.glob('data/data/training/'+str(sub_id)+'*.csv')]#using glob get the files of all files with this subject id
    for trial in range(len(sub_files)):#each file in the list of files for this subject
        # print(trial)
        file_name = [os.path.basename(x) for x in glob.glob('data/data/training/'+str(sub_id)+'_'+list_trials[trial]+'*.csv')]
        # print(file_name)
        #print(file_name[0])
        data = Data()
        try:
            data.add_data(np.genfromtxt('data/data/training/'+str(file_name[0]), delimiter=','))#read the csv
        except:
            break
            pass
        # print(data.data_array)
        data.data_array = data.data_array[:500]
        # print(data.data_array)
        fs = data.calc_sampling_rate()
        hr_data = data.data_array[:,4]#get the ppg signal from data using slicing
        # plt.clf()
        # plt.subplot(121)
        # plt.plot(-hr_data)
        # plt.title(str(sub_id)+" : "+str(trial))
        # plt.show()
        hr_data = HR.preprocess(-hr_data,fs)#preprocess your hr_data:removing baseline, smooth your signal using a low pass filter and normalize. 
        # plt.clf()
        # plt.subplot(122)
        # plt.plot(hr_data)
        # plt.show()
        list_data.append(hr_data)#append the preprocessed data to list_data
        file = [os.path.basename(x) for x in glob.glob('data/data/training/'+str(sub_id)+'_'+list_trials[trial]+'_*.csv')]#retrieve the reference heart rate from the filename.
        file=file[0]
        ref_hr = file[6:9]
        #print(ref_hr)
        list_ref.append(ref_hr)#append the reference heart rate to list_ref
        list_sub.append(sub_id)#append the subject id to list_sub

list_data = np.vstack(list_data)
# i=1
# plt.plot(list_data[i])
# plt.show()
# mu, std = norm.fit(list_data[i])
# plt.hist(list_data[i],density=True, bins=20)
# plt.show()

print(list_data)
print(np.shape(list_data))
print(list_sub)
print(list_ref)


train_data = np.array([])#make empty numpy array of size 0
hold_out_data = np.array([])#make empty numpy array of size 0


# =============================================================================
# for i in range(len(unique_ids[1:])):
#     print(i)
#     train_ids=unique_ids[1:]
#     hold_out_subject = train_ids[i] #for now we’ll hold out the first training subject
#     for ind, sub_id in enumerate(list_sub):#enumerate the list_sub starting at 0. Look up enumerate function
#         # print(ind, sub_id)
#         if sub_id != hold_out_subject:#sub_id is not the same as hold_out_subject) 
#             train_data = np.concatenate((train_data, list_data[ind]))#concatenate numpy array train_data with the list_data at ind
#         else:
#             hold_out_data = np.concatenate((hold_out_data, list_data[ind]))#concatenate numpy array hold_out_data with list_data at ind
#             # plt.plot(hold_out_data)
#             # plt.show()
#     
#     print(np.shape(train_data))
#     print(np.shape(hold_out_data))
#     # print(hold_out_data[i*500:i*500+500])
#     gmm = GMM(n_components = 2).fit(train_data.reshape(-1,1))
#     test_pred = gmm.predict(hold_out_data[i*500:i*500+500].reshape(-1,1))
#     
#     [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(test_pred,fs)
#     plt.clf()
#     plt.plot(test_pred)
#     # print(s_thresh_up)
#     plt.show()
#     print("Estimated BPM = "+str(BPM_Estimate))  
#     
#     print("Real BPM = "+str(list_ref[i*10]))
# 
# =============================================================================
    # plt.clf()
    # plt.plot(hold_out_data[:])
    # plt.plot(test_pred[:])
    # plt.show()
    # plt.hist(hold_out_data[:], density=True, bins=50)
    # plt.show()


# test_pred = gmm.predict(hold_out_data[:].reshape(-1,1))
# print(test_pred)


print("TraingING")

for i in range(len(unique_ids[:])):
    train_ids=unique_ids[:]
    hold_out_subject = train_ids[i]
    for ind, sub_id in enumerate(list_sub):#enumerate the list_sub starting at 0. Look up enumerate function
        # print(ind, sub_id)
        if sub_id != hold_out_subject:#sub_id is not the same as hold_out_subject) 
            train_data = np.concatenate((train_data, list_data[ind]))#concatenate numpy array train_data with the list_data at ind
        else:
            hold_out_data = np.concatenate((hold_out_data, list_data[ind]))#concatenate numpy array hold_out_data with list_data at ind
            # plt.plot(hold_out_data)
            # plt.show()
    
        # print(np.shape(hold_out_data))
        # print(np.shape(train_data))
        try:
            gmm = GMM(n_components = 2).fit(train_data.reshape(-1,1))
        except:
            pass
        
print(np.shape(hold_out_data))

print((hold_out_subject))
for x in range(0,len(hold_out_data),500):
    # print(x)
    trial = hold_out_data[x:x+500]
    # plt.clf()
    # plt.plot(trial)
    # plt.show()
    test_pred = gmm.predict(trial.reshape(-1,1))
    # plt.plot(i)
    # plt.plot(test_pred)
    # plt.show()
    
    # [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(test_pred,fs)
    # plt.clf()
    # plt.plot(test_pred)
    # plt.plot(s_thresh_up)
    # plt.show()
    # print("Estimated BPM = "+str(BPM_Estimate))  

 































# ##testing 

data_array = np.genfromtxt('data/data/testing/09_06_066.csv', delimiter=',')
data = Data()
data.add_data(data_array)
fs = data.calc_sampling_rate()
# print(fs)

hr = data.data_array[:,4]
hr = HR.preprocess(-hr, fs)

plt.clf()
plt.plot(hr)
plt.show()
       
test_pred1 = gmm.predict(hr.reshape(-1,1))
[BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(test_pred1,fs)
plt.clf()
plt.plot(test_pred1)
plt.plot(s_thresh_up)
plt.show()
print("Estimated BPM = "+str(BPM_Estimate))  


print("--- %s seconds ---" % (time.time() - start_time))

















































    
        
        
    
