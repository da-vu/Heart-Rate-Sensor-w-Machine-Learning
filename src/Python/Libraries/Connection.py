# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:50:13 2020

@author: Dan
"""


import serial
import numpy as np
from Libraries.Data import Data #need to import the library you need

class Connection:

    def __init__(self, serial_name, baud_rate):
        self.serial_name = serial_name
        self.baud_rate = baud_rate
        self.data = Data()
        self.setup_connection()
        self.string_buffer = []

    def setup_connection(self): # open serial port
        self.ser = serial.Serial(self.serial_name, self.baud_rate)             
        print(self.ser.name)
    
    def close_connection(self): #close the serial connection
        self.ser.close()                                                       
        
    def send_serial(self, message): #write message to serial
        self.ser.write(message.encode('utf-8'))                                

    def read_serial(self): #read a byte at a time and print to console
        s = self.ser.read(1).decode('utf-8')
        print(s)                                                               
    
    def start_streaming(self): # send 'Start Data\n' through serial
        message = 'start data\n'
        self.send_serial(message)
    
    def receive_data(self):
        c = self.ser.read(1).decode('utf-8')         # read 1 byte
        if( c == '\n'):
            data_string = ''.join(self.string_buffer)
            print(data_string)
            temp_data_array = np.fromstring(data_string,dtype=int,sep=',')
            self.data.add_data(temp_data_array) #using the Data module
            self.string_buffer = []
        else:
           self.string_buffer.append(c)
          
    def end_streaming(self): # send 'Stop Data\n' through serial
        message = 'stop data\n'
        self.send_serial(message)


