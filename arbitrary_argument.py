# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 00:14:03 2019

@author: naveen
"""

#aribitrary argument lists
def write_multiple_items(file,separator,*args):
    file.write(separator.join(args))

#write_multiple_items("sample.txt","/","show","starts","now")

def concat(*args,sep="/"):
    return sep.join(args)
print (concat("earth","mars","venus"))
print(concat("earth","mars","venus",sep="."))