# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:23:55 2020

@author: Dan
"""

import numpy as np
print (np.__version__)


# =============================================================================
# test_array = np.array([0,10,4,12])
# 
# print(test_array-20)
# print(test_array.shape)
# print(test_array.dtype)
# =============================================================================


# =============================================================================
# test_2D_array = np.array([(0,10,4,12),
#                           (1,20,3,41)])
# print(test_2D_array.shape)
# =============================================================================


# =============================================================================
# print(np.zeros((10,20)))
# =============================================================================


# =============================================================================
# test_array = np.array([0,10,4,12])
#  
# h_arr = np.hstack((test_array, test_array))
# 
# v_arr = np.vstack((h_arr,h_arr))
# 
# final_arr =np.vstack((v_arr,v_arr))
# 
# print(final_arr)
# =============================================================================


# =============================================================================
# arange_array1 = np.arange(-3,16,6)
# arange_array2 = np.arange(-7,-20,-2)
# print(arange_array1)
# print(arange_array2)
# =============================================================================

# =============================================================================
# linspace_array = np.linspace(0,100,num=49)
# print(linspace_array)
# =============================================================================

# =============================================================================
# e = np.zeros((3,4))
# e[1,0] = 0
# e[:,1] = [3, 0, 2]
# e[2, :2] = [4, 2]
# e[2, 2:] = [3,2]
# e[:,2] = [1,1,3]
# e[1,3] = 2
# 
# print(e)
# =============================================================================

s = '1,2,3,4'
print(s)
arr = np.fromstring(s,dtype=int,sep=',')
final_array = arr
for x in range(100):
    final_array = np.vstack((final_array,arr))

print(final_array)