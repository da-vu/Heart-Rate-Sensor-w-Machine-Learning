# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 02:07:30 2020

@author: Dan
"""


import matplotlib.pyplot as plt
import numpy as np

# =============================================================================
# plt.clf() #clear any existing plot
# plt.plot([1,2,3,4],[1,4,9,16])
# plt.show()
# =============================================================================

a = np.array([[1,2,3,4],[1,4,9,16]])
x = a[0,:]
y = a[1,:]
print(x,y)
plt.clf()
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.show()


a = np.array([[1,2,3,4],[1,4,9,16]])
b = np.array([[1,2,3,4],[4,2,1,6]])

plt.clf()
plt.subplot(211)
plt.plot(a[0,:],a[1,:]) #fill in ax and ay
plt.subplot(212)
plt.plot(b[0,:],b[1,:]) #fill in bx and by
plt.show()
