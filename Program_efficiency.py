## -*- coding: utf-8 -*-
#"""
#Created on Mon Jun 10 20:21:19 2019
#
#@author: naveen
#"""
##UNDERSTNDING PROGRAM EFFICIENCY
#import time
#def mysum(x):#function definition
#    total=0#1-Operation
#    for i in range(x+1):#1-operation
#        total+=i#Two operations
#    return total
##total operations= 1+3x
#print mysum(5)
#
##Different input change how the program runs
##A function searches for an element in the list
#def search_for_elmt(L,e):
#    for i in L:
#        if i==e:
#            return True#function returns only one object
#    return False
#    
L=[2,4,5,6,12,15,65,69,98]
LU=[4,2,12,5,44,76,23,5,1,16]
LR=[98,69,65,15,12,6,5,4,2]
#t0=time.clock()
#print search_for_elmt(L,0)
#t1=time.clock()
##print("Time taken:",t1-t0)
##Common algorithms
#
#Linear search on unsorted lisg
#def linear_search(L,e):
#    found=False
#    for i in range(len(L)):
#        if e==L[i]:
#            found=True
#    return found

def linear_search_sorted(L,e):
    
    for i in range(len(L)):
        if L[i]==e:
            return True
        if L[i]>e:
            return False
    return False

t0=time.clock()
#print(linear_search(LU,16))
#print(linear_search_sorted(L,55))
t1=time.clock()
print("Time taken:",t1-t0)

#Quadratic complexity
#Nested loop, len(L1)*len(L2)
def isSubset(L1,L2):
    for e1 in L1:
        matched=False
        for e2 in L2:
            if e1==e2:
                matched=True
                break
        if not matched:
            return False
    return True
L1=[2,3,4,5,6,7,8,7]
L2=[1,2,3,4,5,6,7,8,9,11,13,14]
print(isSubset(L1,L2))

def intersect(L1,L2):
    tmp=[]
    for e1 in L1:
        for e2 in L2:
            if e1==e2:
                tmp.append(e1)
    res=[]
    for e in tmp:#this loop is to remove duplicates
        if not (e in res):
            res.append(e)
    return res
print intersect(L1,L2)
            