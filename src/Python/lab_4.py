# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:26:08 2020

@author: Dan
"""
import matplotlib.pyplot as plt
import numpy as np
import serial
import time

#Make the variables below global
string_buffer = []
data_array = np.array([])
sample_number = 0


def setup_serial():
    serial_name = 'COM3'
    # serial_name = '/dev/cu.usbserial-143230'
    # serial_name = '/dev/cu.DAVU_FireBeetle-ESP32SPP'
    ser = serial.Serial(serial_name, 115200)  # open serial port
    print(ser.name)         # check which port was really used
    return ser


def read_serial4(ser):
    while True:
        try:
            s = ser.read(1).decode('utf-8')         # read 1 byte and decode to utf-8
            print(s)
        except(KeyboardInterrupt):
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break

def receive_data(ser):
    # Send start data
# =============================================================================
#     S_List = ['start',' data', '\n']
#     for S in S_List:
#         ser.write(S.encode('utf-8'))
# =============================================================================
    s = 'start data\n'
    ser.write(s.encode('utf-8'))
    while sample_number < 500:
        try:
            receive_sample(ser)
        except(KeyboardInterrupt):
            # Send stop data 
# =============================================================================
#             S_List = ['stop',' data','\n']
#             for S in S_List:
#                 ser.write(S.encode('utf-8'))
# =============================================================================
            s1 = 'stop data\n'
            ser.write(s1.encode('utf-8'))
            time.sleep(2)
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break
# =============================================================================
#     S_List = ['stop',' data','\n']
#     for S in S_List:
#         ser.write(S.encode('utf-8'))
# =============================================================================
    s1 = 'stop data\n'
    ser.write(s1.encode('utf-8'))
    time.sleep(2)
    ser.close()
    return data_array

def calc_sampling_rate(data_array):
    time_arr = data_array[:,0]
    print("SAMPLING RATE IS: ")

    mean_diff = np.mean(np.diff(time_arr,1,0))
    print(1000000/mean_diff)
    
        
def receive_sample(ser):
    global string_buffer
    global data_array
    global sample_number
    
    # read a byte from serial (remember to decode)
    c = ser.read(1).decode('utf-8') #read_serial4(ser);
    if(c == '\n'):
        sample_number = sample_number + 1
        data_string = ''.join(string_buffer)
        print(data_string)
        temp_data_array = np.fromstring(data_string,sep=',')#csv string to 1x4 np array
        if (data_array.size == 0): 
            data_array = temp_data_array
        else:
            data_array =  np.vstack((data_array,temp_data_array))#vstack temp_data_array to end of data_array
        string_buffer = [] # reset buffer to []
    else:
       string_buffer.append(c)# append the new char to string_buffer
       
def moving_average(s,n_avg):
    ma = np.zeros(s.size) 
    for i in np.arange(0,len(s)):
      ma[i] =  np.average(s[i:i+n_avg])   #mean of s from index i to i+n_avg
    return ma

def detrend(s,n_avg): #remove the moving average from the signal
    ma = moving_average(s,n_avg)
    return s-ma #s minus the moving_average



def signal_diff(s):
    s_diff = np.diff(s) #calculate the gradient using np.diff
    s_diff = np.append(s_diff, 0) #np.diff returns one shorter, so need to add a 0
    return s_diff

def plotData(data_array):
    time = data_array_saved[:,0]
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



if __name__== "__main__":
# =============================================================================
#     ser = setup_serial()
#     data_array = receive_data(ser)
#     calc_sampling_rate(data_array)
#     ser.close()
#     
#     np.savetxt("data_1.csv", data_array, delimiter=",")
# =============================================================================
    data_array_saved = np.genfromtxt('data_01_072.csv', delimiter=',')  
    
    
# =============================================================================
#     time = data_array_saved[:,0]
#     x = data_array_saved[:,1]
#     y = data_array_saved[:,2]
#     z = data_array_saved[:,3]
#     
#     
#     plt.clf()
#     plt.subplot(311)
#     plt.xlabel("time")
#     plt.ylabel("x")
#     plt.plot(time,x)
#     plt.subplot(312)
#     plt.xlabel("time")
#     plt.ylabel("y")
#     plt.plot(time,y) 
#     plt.subplot(313)
#     plt.xlabel("time")
#     plt.ylabel("z")
#     plt.plot(time,z)
#     plt.tight_layout()
#     plt.show()
# =============================================================================
    
    plotData(data_array_saved)
    time = data_array_saved[:,0]
    
# =============================================================================
#     s = data_array_saved[:,4] #get the z 
#     plt.plot(time,s)
#     mean_s = np.average(s)
#     s = s-mean_s
#     plt.plot(time,s)
#     plt.show()
#     
#     plt.clf()
#     plt.plot(time,moving_average(s,2))
#     plt.show()
#     
#     plt.clf()
#     plt.plot(time,detrend(s,20))
#     plt.title('n_avg=20')
#     plt.show()
#     
#     plt.clf()
#     plt.plot(time,signal_diff(s))
#     plt.title('using signal_diff')
#     plt.show()
# =============================================================================
    
    
    
    
    
    



































