# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:26:08 2020

@author: Dan
"""
import numpy as np
import serial

#Make the variables below global
string_buffer = []
data_array = np.array([])



def setup_serial():
    serial_name = 'COM3'
    ser = serial.Serial(serial_name, 9600)  # open serial port
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
    S_List = ['start',' data', '\n']
    for S in S_List:
        ser.write(S.encode('utf-8'))
    while True:
        try:
            receive_sample(ser)
        except(KeyboardInterrupt):
            # Send stop data 
            S_List = ['stop',' data','\n']
            for S in S_List:
                ser.write(S.encode('utf-8'))
            ser.close() #we'll use ctrl+c to stop the program
            print("Exiting program due to KeyboardInterrupt")
            break
   
        
def receive_sample(ser):
    global string_buffer
    global data_array
    
    # read a byte from serial (remember to decode)
    s = ser.read(1).decode('utf-8') #read_serial4(ser);
    if(s == '\n'):
        data_string = ''.join(string_buffer)
        print(data_string)
        temp_data_array = np.fromstring(data_string,sep=',')#csv string to 1x4 np array
        if (data_array.size == 0): 
            data_array = temp_data_array
        else:
            data_array =  np.vstack((data_array,temp_data_array))#vstack temp_data_array to end of data_array
        string_buffer = [] # reset buffer to []
    else:
       string_buffer.append(s)# append the new char to string_buffer
      
if __name__== "__main__":
    ser = setup_serial()
    receive_data(ser);



