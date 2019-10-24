# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 12:36:48 2019

@author: naveen
"""
#give the fibonaccin numbers in that region
def fib(n):
    a,b=0,1
    while a<n:
        print(a,end=' ')        
        a,b=b,a+b
    print()
fib(20)

#gives that number of fibonacci numbers in series
def fib1(n):
    a,b=0,1
    for i in range(0,n):
        print(a)
        a,b=b,a+b
        
f=fib1
f(5)

def fib2(n):
    """return a list conatining fibonacci series upto n"""
    result=[]
    a,b=0,1
    while a<n:
        result.append(a)
        a,b=b,a+b
    return result

print (fib2(50))#returns a list consists of fibonacci numbers 

#more on functions
#def ask_ok(prompt, retries=4, remainder="Please try again"):
#    while True:
#        ok = input(prompt)
#        if ok in ('y','yes','yep'):
#            return True
#        if ok in ('n','no','nop'):
#            return False
#        retries-=1
#        if retries<0:
#            raise ValueError("invalid user response")
#        print(remainder)
#print(ask_ok('Do you really want to quit?:',4))

i=5
def f(arg=i):
    print (arg)
i=6
f()

#the default value is evaluated only once. This makes difference when the default is a
#mutable object such as a list, dictionary or instances of most classes
def f(a,L=[]):
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))

def f(a,L=None):
    if L is None:
        L=[]     #list is become emptied 
        each time 
    L.append(a)
    return L
print(f(1))
print(f(2))
print(f(3))