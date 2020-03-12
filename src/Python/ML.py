# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 21:38:02 2020

@author: Dan
"""



import glob
import os
#from Libraries.Connection import Connection
from Libraries.Visualize import Visualize
from Libraries.HR import HR
from Libraries.Data import Data
import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture as GMM
import time
start_time = time.time()


unique_ids = []

all_files = [os.path.basename(x) for x in glob.glob('data/data/TRASH/*.csv')]#the correct regex)
# print(all_files)#check what is in your all_files by printing. You should get a list of strings of the filenames.


for file in all_files:
    sub_id = file[:2]
    if sub_id not in unique_ids:
        unique_ids.append(sub_id)

    


list_data = []
list_sub = []
list_ref = []
list_trials = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']


for sub_id in unique_ids:#sub_id in the list of unique_ids
    sub_files = [os.path.basename(x) for x in glob.glob('data/data/TRASH/'+str(sub_id)+'*.csv')]#using glob get the files of all files with this subject id
    for trial in range(len(sub_files)):#each file in the list of files for this subject
        # print(trial)
        file_name = [os.path.basename(x) for x in glob.glob('data/data/TRASH/'+str(sub_id)+'_'+list_trials[trial]+'*.csv')]
        # print(file_name)
        #print(file_name[0])
        data = Data()
        try:
            data.add_data(np.genfromtxt('data/data/TRASH/'+str(file_name[0]), delimiter=','))#read the csv
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
        file = [os.path.basename(x) for x in glob.glob('data/data/TRASH/'+str(sub_id)+'_'+list_trials[trial]+'_*.csv')]#retrieve the reference heart rate from the filename.
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

print("\nunique ids:")
print(unique_ids)
print("\nlist_data")
print(list_data)
print("\nshape of list_data")
print(np.shape(list_data))
print("\nlist_sub")
print(list_sub)
print("\nlist_ref")
print(list_ref)
print(np.size(list_ref))


train_data = np.array([])#make empty numpy array of size 0
hold_out_data = np.array([])#make empty numpy array of size 0


print(" NOW TRAINING")

for i in range(len(unique_ids[:])):
    train_ids=unique_ids[:]
    hold_out_subject = train_ids[i]
    for ind, sub_id in enumerate(list_sub):#enumerate the list_sub starting at 0. Look up enumerate function
        if sub_id != hold_out_subject:#sub_id is not the same as hold_out_subject) 
            train_data = np.concatenate((train_data, list_data[ind]))#concatenate numpy array train_data with the list_data at ind
        else:
            hold_out_data = np.concatenate((hold_out_data, list_data[ind]))#concatenate numpy array hold_out_data with list_data at ind
            
        try:
            gmm = GMM(n_components = 2).fit(train_data.reshape(-1,1))
        except:
            pass
           
print(" DONE TRAINING")

print("\nShape of hold_out_data & elements of hold_out_data")
print(np.shape(hold_out_data))
print(hold_out_data)

list_bpm =[]
for x in range(0,len(hold_out_data),500):
    trial = hold_out_data[x:x+500]
    fig = plt.gcf()
    fig.set_size_inches(8, 4)
    plt.clf()
    plt.subplot(121)
    plt.plot(trial)
    # plt.title("\nPreprocessed heart signal\n Trial #=" +str(int((x/500)+1)))
    plt.title("\nPreprocessed heart signal\n Reference BPM=" +list_ref[int((x/500))])
    test_pred = gmm.predict(trial.reshape(-1,1))
   
    [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(test_pred,fs)
    plt.subplot(122)
    plt.plot(test_pred)
    plt.plot(s_thresh_up)
    plt.title("\nThreshold and prediction test\n Estimated BPM = "+str(BPM_Estimate))
    plt.show()
    list_bpm.append(BPM_Estimate) 


print("\nList_bpm - Estimated BPM of validation sets from trained model") 
print(list_bpm)

int_ref=[]

for ref in list_ref:
    ref = float(ref)
    int_ref.append(ref)


ref_arr=np.array(int_ref)
print(ref_arr)
bpm_arr=np.array(list_bpm)


ref_arr=np.reshape(int_ref,(len(int_ref),1))
bpm_arr=np.reshape(list_bpm,(len(list_bpm),1))

arrr = np.hstack((ref_arr,bpm_arr))
arrr = np.reshape(arrr,(30,2))

Visualize.plotBandAltmann(arrr)

























# =============================================================================
# =============================================================================
# =============================================================================
# # # 
# # # # ##testing 
# # # 
# # # data_array = np.genfromtxt('data/data/testing/09_06_066.csv', delimiter=',')
# # # data = Data()
# # # data.add_data(data_array)
# # # fs = data.calc_sampling_rate()
# # # # print(fs)
# # # 
# # # hr = data.data_array[:,4]
# # # hr = HR.preprocess(-hr, fs)
# # # 
# # # plt.clf()
# # # plt.plot(hr)
# # # plt.show()
# # #        
# # # test_pred1 = gmm.predict(hr.reshape(-1,1))
# # # [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(test_pred1,fs)
# # # plt.clf()
# # # plt.plot(test_pred1)
# # # plt.plot(s_thresh_up)
# # # plt.show()
# # # print("Estimated BPM = "+str(BPM_Estimate))  
# # # 
# # # 
# # # print("--- %s seconds ---" % (time.time() - start_time))
# =============================================================================
# =============================================================================
# =============================================================================

















































    
        
        
    
