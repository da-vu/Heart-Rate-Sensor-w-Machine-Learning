import glob
import os
from Libraries.HR import HR
from Libraries.Data import Data
from Libraries.Visualize import Visualize
import matplotlib.pyplot as plt
import numpy as np
from sklearn.mixture import GaussianMixture as GMM


# ../data/data/training/ 

class ML:
    def __init__(self):
        self.gmm = GMM(n_components = 2)
        

    def train_hr_model(self, directory):
        print(directory)
        unique_ids = []
        # all_files = [os.path.basename(x) for x in glob.glob('data/data/training/*.csv')]#the correct regex)
        all_files = [os.path.basename(x) for x in glob.glob(directory+'*.csv')]#the correct regex)
        # print(all_files)
        
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
            sub_files = [os.path.basename(x) for x in glob.glob(directory+str(sub_id)+'*.csv')]#using glob get the files of all files with this subject id
            for trial in range(len(sub_files)):#each file in the list of files for this subject
                file_name = [os.path.basename(x) for x in glob.glob(directory+str(sub_id)+'_'+list_trials[trial]+'*.csv')]
                # print(file_name)
                data = Data()
                try:
                    data.add_data(np.genfromtxt(directory+str(file_name[0]), delimiter=','))#read the csv
                except:
                    break
                    pass
                data.data_array = data.data_array[:500]
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
                file = [os.path.basename(x) for x in glob.glob(directory+str(sub_id)+'_'+list_trials[trial]+'_*.csv')]#retrieve the reference heart rate from the filename.
                file=file[0]
                ref_hr = file[6:9]
                list_ref.append(ref_hr)#append the reference heart rate to list_ref
                list_sub.append(sub_id)#append the subject id to list_sub
                
        list_data = np.vstack(list_data)
        print(list_data)
        print(np.shape(list_data))
        print(list_sub)
        print(list_ref)
        
        
        
        
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
                    self.gmm = GMM(n_components = 2).fit(train_data.reshape(-1,1))
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
            test_pred = self.gmm.predict(trial.reshape(-1,1))
           
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

        
        

    def calc_hr(self,s,fs):
        fig = plt.gcf()
        fig.set_size_inches(12, 4)
        plt.clf()
        plt.subplot(131)
        plt.plot(s.data_array[:,4])
        plt.title("Original HR signal")
        
        shr = s.data_array[:,4]
        shr = HR.preprocess(-shr, fs)
        plt.subplot(132)
        plt.plot(shr)
        plt.title("Preprocessed HR signal")
       
        
        test_pred = self.gmm.predict(shr.reshape(-1,1))
        ##fixy
        unique,counts=np.unique(test_pred, return_counts=True)
        # print(unique,counts)
        if counts[0] < counts[1]:
            # print("flip time")
            test_pred = -test_pred + 1
        ##fixy
        [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(test_pred,fs)
        plt.subplot(133)
        plt.plot(test_pred)
        plt.plot(s_thresh_up)
        plt.title("Estimated BPM according to GMM\n Estimated BPM = "+str(BPM_Estimate))
        plt.show()
        print("Estimated BPM = "+str(BPM_Estimate))  
        return BPM_Estimate
    
    
    
    
    
    
    
    def test_hr_model(self,directory):
        print(directory)
        unique_ids = []
        unique_trial = []
        ref_hr = []
        esthr=[]
        arr=np.array([])
        all_files = [os.path.basename(x) for x in glob.glob(directory+'*.csv')]#the correct regex)
        
        
        for file in all_files:
            sub_id = file[:2]
            if sub_id not in unique_ids:
                unique_ids.append(sub_id)
                
        print(unique_ids)
        for file in all_files:
            trial = file[3:5]
            if trial not in unique_trial:
                unique_trial.append(trial)
                
        for file in all_files:
            heartbeat = file[6:9]
            ref_hr.append(heartbeat)
        
        i=0
        for num in range(len(unique_ids)):
            for trial in range(len(unique_trial)):
                file_name = str(unique_ids[num])+'_'+str(unique_trial[trial])+'_'+str(ref_hr[i]+'.csv')
                print(file_name)
                raw_data=np.genfromtxt(directory+file_name, delimiter=',')
                raw_data=raw_data[:500]
                raw_data_obj = Data()
                raw_data_obj.add_data(raw_data)
                fs = raw_data_obj.calc_sampling_rate()
                i=i+1
                esthr.append(self.calc_hr(raw_data_obj, fs))
                
        
        ref_hr = []
        for file in all_files:
            heartbeat = float(file[6:9])
            ref_hr.append(heartbeat)
        
        ref_arr=np.array(ref_hr)    
        est_arr=np.array(esthr)  
       
        
        ref_arr=np.reshape(ref_arr,(ref_arr.size,1))
        est_arr=np.reshape(est_arr,(est_arr.size,1))
       
        arr = np.hstack((ref_arr,est_arr))
        arr= np.reshape(arr,(10,2))
        
        print(np.shape(arr))
        Visualize.plotBandAltmann(arr)
        
        return arr
            
                
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
     