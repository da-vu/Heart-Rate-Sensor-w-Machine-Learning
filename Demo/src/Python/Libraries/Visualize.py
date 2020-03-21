# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 17:24:17 2020

@author: Dan
"""
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import numpy as np

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
        
    def plotBandAltmann(data_array):
        gnd =  data_array[:,0] #reference heart rate
        est =  data_array[:,1] #estimate of your algorithm
        
        [R,p] = pearsonr(gnd,est)
        RMSE = np.sqrt(np.mean((est-gnd)**2))
        
        plt.figure(1)
        plt.clf()
        plt.subplot(121)
        plt.plot(gnd,gnd)
        plt.scatter(gnd,est)
        plt.text(min(gnd) + 2,max(est)+2,"R="+str(round(R,2))+", RMSE="+str(round(RMSE,3)))
        plt.ylabel("estimate HR (BPM)")
        plt.xlabel("reference HR (BPM)")
        
        avg = np.mean(np.array([ gnd, est ]), axis=0 )#take the average of gnd and est
        dif =  (gnd-est)#take the difference of gnd and est
        std =  np.std(dif)#get the standard deviation of the difference (using np.std)
        bias = np.mean(dif)#the mean value of the difference
        upper_std = (bias+1.96*std) #the bias plus 1.96 times the std
        lower_std = (bias-1.96*std)#the bias minus 1.96 times the std
        
        plt.subplot(122)
        plt.scatter(avg, dif)
        plt.plot([np.min(avg),np.max(avg)],[bias,bias])
        plt.plot([np.min(avg),np.max(avg)],[upper_std, upper_std])
        plt.plot([np.min(avg),np.max(avg)],[lower_std, lower_std])
        plt.text(np.max(avg)+5,bias,"mean="+str(round(np.mean(gnd-est),2)))
        plt.text(np.max(avg)+5,upper_std,"1.96STD="+str(round(upper_std,2)))
        plt.text(np.max(avg)+5,lower_std,"-1.96STD="+str(round(lower_std,2)))
        plt.ylabel("Difference of Est and Gnd (BPM)")
        plt.xlabel("Average of Est and Gnd (BPM)")
        
        plt.show()
            
        
    
