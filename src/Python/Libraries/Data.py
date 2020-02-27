# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:12:34 2020

@author: Dan
"""
import numpy as np


class Data:
    
    def __init__(self):
        self.data_array = np.array([])
        
    
    def add_data(self, new_data): #check the number of samples using get_num_samples and add the new data into the data_array accordingly. 
        if (self.get_num_samples() == 0): 
            data_array = new_data
        else:
            data_array =  np.vstack((data_array,new_data))#vstack temp_data_array to end of data_array
            
            
    def clear_data(self): # reset data_array to empty np array
        self.data_array = np.array([]) 
        
    def get_num_samples(self): # return the size of data_array
        return self.data_array.size 
        
    def calc_sampling_rate(self):
        time_arr = self.data_array[:,0]
        print('SAMPLING RATE IS: ')

        mean_diff = np.mean(np.diff(time_arr,1,0))
        print(1000000/mean_diff)
        
        