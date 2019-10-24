# -*- coding: utf-8 -*-
"""
Created on Fri May 31 00:47:23 2019

@author: naveen
"""

# function as argument
def function_a():
    print("inside_function_a")
def function_b(y):
    print "inside_function_b"
    return y
def function_c(z):
    print "inside function_c"
    return z
    
print function_a
print function_b(2)
print function_c(function_a())