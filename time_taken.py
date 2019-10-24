# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 19:07:09 2019

@author: naveen
"""

import time

def c_to_f(c):
    return c*9/5+32
t0=time.clock()
c_to_f(10000)
t1=time.clock()
print("t=",t0,":",t1,"s", t1-t0)


