# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:50:38 2020

@author: Dan
"""

from Libraries.Connection import Connection
from Libraries.Visualize import Visualize
from Libraries.HR import HR
from Libraries.Data import Data
from Libraries.ML import ML
import matplotlib.pyplot as plt
import numpy as np

class Wearable:
    def __init__(self, serial_name, baud_rate):
        self.connection = Connection(serial_name, baud_rate)
    
    def collect_data(self, num_samples):
        self.connection.end_streaming()
        self.connection.start_streaming()
        while self.connection.data.get_num_samples() < num_samples:
            try:
                self.connection.receive_data()
            except(KeyboardInterrupt):
                self.connection.end_streaming()
                self.connection.close_connection()
                print("Exiting program due to KeyboardInterrupt")
                break
        self.connection.end_streaming()
    
    def main(self):
        self.collect_data(500)
        self.connection.close_connection()
        collected_data = self.connection.data
        fs = int(collected_data.calc_sampling_rate()) #round to nearest int
        np.savetxt("data_file.csv", collected_data.data_array, delimiter=",")
        data_array = np.genfromtxt('data_file.csv', delimiter=',')
        [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(data_array[:,4],fs)
        time = (data_array[:,0] - data_array[0,0])/1e6 #have time start at 0 and in seconds
        plt.clf()
        plt.plot(time, HR.normalize_signal(HR.detrend(-data_array[:,4],fs)))
        plt.plot(time, s_thresh_up)
        print("BPM = "+str(BPM_Estimate))      
        

def ML_main():
    ml = ML()
    ml.train_hr_model('data/data/TRASH/')
    ml.test_hr_model('data/data/testing/')
    

        
            

def main():
    serial_name = 'COM5'
    # serial_name = '/dev/cu.usbserial-143220'
    baud_rate = 115200
    wearable = Wearable(serial_name, baud_rate)
    wearable.main()
    
    # data_array_600 = np.genfromtxt('data/02_01_071.csv', delimiter=',')
    # data_array = data_array_600[:500]
    # # Visualize.plotData(data_array)
    # data = Data()
    # data.add_data(data_array)
    # print(data.get_num_samples())
    # fs = int(data.calc_sampling_rate())
    # [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(data_array[:,4],fs)
    # time = (data_array[:,0] - data_array[0,0])/1e6 #have time start at 0 and in seconds
    # plt.clf()
    # plt.plot(data.data_array[:,4])
    # plt.show()
    # plt.clf()
    # plt.plot(HR.normalize_signal(data.data_array[:,4]))
    # plt.show()
    # plt.clf()
    # plt.plot(HR.moving_average(data.data_array[:,4],fs))
    # plt.show()
    # plt.clf()
    # plt.plot(HR.signal_diff(data.data_array[:,4]))
    # plt.show()
    # plt.clf()
    # plt.plot(HR.detrend(data.data_array[:,4],fs))
    # plt.show()
    
    # print("BPM = "+str(BPM_Estimate))
    
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
# # # #     data_array_600 = np.genfromtxt('data/data_10_083.csv', delimiter=',')
# # # #     data_array = data_array_600[:500]
# # # #     Visualize.plotData(data_array)
# # # #     data = Data()
# # # #     data.add_data(data_array)
# # # #     print(data.get_num_samples())
# # # #     fs = int(data.calc_sampling_rate())
# # # #     
# # # #     [BPM_Estimate, s_thresh_up] = HR.calc_heart_rate_time(data_array[:,4],fs)
# # # #     time = (data_array[:,0] - data_array[0,0])/1e6 #have time start at 0 and in seconds
# # # #     # print(len(time))
# # # #     plt.clf()
# # # #     plt.plot(time, HR.normalize_signal(HR.signal_diff(-data_array[:,4])))
# # # #     plt.plot(time, s_thresh_up)
# # # #     print("BPM = "+str(BPM_Estimate)) 
# # # #     
# =============================================================================
# =============================================================================
# =============================================================================
# =============================================================================
    
    # HR.calc_heart_rate_freq(data_array[:,4], fs)
    
    # plt.clf()
    # plt.plot(data_array[:,4])
    # plt.show()
    
    

    # ml = ML()
    # ml.train_hr_model('data/data/TRASH/')
    # ml.test_hr_model('data/data/testing/')
    
    
    
    

if __name__== "__main__":
    ML_main()


