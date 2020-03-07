# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:24:17 2020

@author: Dan
"""
import matplotlib.pyplot as plt

class Visualize:
    def plotData(data_array): #plot the 3 axis accelerometer data and the heart pulse data into 4 subplots
        time = data_array[:,0]
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
        
    def plotAccel(data_array): # plot the 3 axis accelerometer data.
        time = data_array[:,0]
        plt.clf()
        plt.subplot(311)
        
        plt.title("Example Data Plot")
        
        plt.plot(time,data_array[:,1])
        
        plt.ylabel("X Amplitude")
        
        plt.subplot(312)
        plt.plot(time,data_array[:,2])
        plt.ylabel("Y Amplitude")
        
        plt.subplot(313)
        plt.plot(time,data_array[:,3])
        plt.ylabel("Z Amplitude")
        plt.xlabel(u'Time(${\mu}s$)')
        
        plt.tight_layout() 
        plt.show()
        

    def plotHr(data_array): # plot the heart pulse data
        time = data_array[:,0]
        plt.clf()
        plt.plot(time,-data_array[:,4])
        
        plt.xlabel(u'Time(${\mu}s$)')
        plt.ylabel("R Amplitude")

        plt.show()
        
        
        
    
