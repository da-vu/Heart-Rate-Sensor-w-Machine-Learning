# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 21:20:55 2020

@author: Dan
"""
import numpy as np

incoming_stream = b'1',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'2',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'3',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'4',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'5',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'6',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'7',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'8',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'9',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n',b'1',b'0',b'0',b'0',b'0',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b',',b'1',b'2',b'3',b'4',b'\n'

string_buffer = []
data_array = np.array([])

for incoming_byte in incoming_stream:
    c = incoming_byte.decode('utf-8') #this takes the place of reading the byte from serial
    if( c == '\n'):
        data_string = ''.join(string_buffer)
        print(data_string)
        temp_data_array = np.fromstring(data_string,sep=',')#csv string to 1x4 np array
# =============================================================================
#         if (data_array.size == 0): 
#             data_array = temp_data_array
#         else:
# =============================================================================
        data_array =  np.vstack((data_array,temp_data_array))#vstack temp_data_array to end of data_array
        string_buffer = [] # reset buffer to []
    else:
       string_buffer.append(c)# append the new char to string_buffer

