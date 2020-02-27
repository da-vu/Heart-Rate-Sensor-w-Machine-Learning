# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:50:38 2020

@author: Dan
"""
from Libraries.Connection import Connection
from Libraries.Visualize import Visualize
import numpy as np

class Wearable:
    def __init__(self, serial_name, baud_rate):
        self.connection = Connection(serial_name, baud_rate)
    
    def collect_data(self, num_samples):
        #first make sure data sending is stopped by ending streaming
        self.connection.end_streaming()
        #start sending data
        self.connection.start_streaming()
        while self.connection.data.get_num_samples() < num_samples: #collect x samples
            try:
                #receive data
                self.connection.receive_data()
            except(KeyboardInterrupt):
                #deal with exception
                print("Exiting program due to KeyboardInterrupt")
                break
        #end streaming
        self.connection.end_streaming()
        
    def main(self):
        num_samples = 500
        self.collect_data(num_samples)
        #calculate sampling rate
        self.connection.data.calc_sampling_rate()
        #save data data_array1 = self.connection.data.data_array
        np.savetxt("data_1.csv", self.connection.data.data_array, delimiter=",")
        #read data
        data_array1 = np.genfromtxt('data_1.csv', delimiter=',') 
        Visualize.plotData(data_array1)
        self.connection.close_connection()
        
            

def main():
    serial_name = 'COM3'
    baud_rate = 115200
    wearable = Wearable(serial_name, baud_rate)
    wearable.main()


if __name__== "__main__":
    main()
