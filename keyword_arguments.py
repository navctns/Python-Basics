# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 23:49:36 2019

@author: naveen
"""

def cheeseshop(kind,*argument,**keywords):
    print("-- Do you havy any",kind,"?")
    print("-- Im sorry we're all out of",kind)
    for arg in argument:
        print(arg)
    print("-"*40)
    for kw in keywords:
        print(kw,":",keywords[kw])

cheeseshop("Limburger","It's very runny, sir",
           "It's very, VERY, runny, Sir",#it is positional arguments
           shopkeeper="Michael Palin",#keyword aruguments specified with keyword
           client="John cleese",
           sketch="Cheeseshop sketch")
           
               