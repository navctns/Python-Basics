# -*- coding: utf-8 -*-
"""
Created on Fri May 31 00:34:01 2019

@author: naveen
"""

#different functions
#with return
def is_even_with_return(i):
    """
    input :i, a positive integer
    Retrun True is i is even, otherwise return False
    """
    print "with return"
    remainder=i%2
    return remainder==0
    
num=int(input("Enter a number:"))
print(is_even_with_return(num))

#without return
def is_even_without_return(i):
    """
    input: i, a positive integer
    Nothing returns
    """
    print "Without retrun"
    remainder=i%2
    
print(is_even_without_return(3))