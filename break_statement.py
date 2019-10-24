# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:15:09 2019

@author: naveen
"""

for n in range(2,10):
    for x in range(2,n):
        if n%x==0:
            print(n,"equals",x,'*',n//x)
            break
    else:
        print(n,"is a prime number")
        
#continue statement
    
for num in range(2,10):
    if num%2==0:
        print("Found an even number:",num)
        continue
    print("found a number:",num)