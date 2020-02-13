# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:26:08 2020

@author: Dan
"""
import numpy as np
import serial
import time

#Make the variables below global
string_buffer = []
data_array = np.array([])
sample_number = 0


def setup_serial():
    # serial_name = 'COM3'
    # serial_name = '/dev/cu.usbserial-143230'
    serial_name = '/dev/cu.DAVU_FireBeetle-ESP32SPP'
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
    while sample_number < 100:
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
    return data_array

def calc_sampling_rate(data_array):
    time_arr = data_array[:,0]
    print("SAMPLING RATE IS: ")
    diff_arr = np.diff(time_arr)
    sper = np.mean(diff_arr) * 1000000
    srate = (1 / sper) 
    print(srate)
    
        
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
      
if __name__== "__main__":
    ser = setup_serial()
    s1 = 'stop data\n'
    ser.write(s1.encode('utf-8'))
    data_array = receive_data(ser)
    calc_sampling_rate(data_array)
    s1 = 'stop data\n'
    ser.write(s1.encode('utf-8'))
    time.sleep(3)
    ser.close()

