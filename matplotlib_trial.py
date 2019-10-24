# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 21:47:22 2019

@author: naveen
"""

#matplotlib
import numpy as np
import matplotlib.pyplot as plt
#generate sequence of numbers -10 to 10 with 100 steps in between
x=np.linspace(-10,10,100)
#create a second array using sine
y=np.sin(x)
#The plot function makes a line chart of one array aginst another
plt.plot(x,y,marker="x")