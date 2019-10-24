# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 21:32:35 2019

@author: naveen
"""

#Testing, debugging, Exception and Assertions
def abs_val(x):
    """ Assumes X is an int, Returns x if x>=0 and -x otherwise"""
    if x<-1:
        return -x
    else:
        return x
        
#print abs_val(2)
#print abs_val(-2)
#print abs_val(-1)

#the function incorrectly runs for input -1

#EXCEPIONs
#Any code in program you might think problematic that might give you an error
# or exception , write in try block

#try:
#    a=int(input("Tell me one number:"))
#    b=int(input("Tell me another number:"))
#    print(a/b)
#except:
#    print("Bug in user input")

#HANDLING SPECIFIC EXCEPTIONS

#have separate clauses to deal with a particular type of exception

#try:
#    a=int(input("Tell me one number:"))
#    b=int(input("Tell me another number:"))
#    print("a/b=",a/b)
#    print("a+b=",a+b)
#
#except ValueError:
#    print("Could not convert to a number")
#except ZeroDivisionError:
#    print("cannot divide by zero")
#except:
#    print "Something went very wrong"

#Raise an exception 
# raise<exception Name>(<arguments>)

#EXCEPTION AS CONTROL FLOW
#def get_ratios(L1,L2):
#    
#    """ Assume: L1 and L2 are lists of equal length of numbers
#    Returns: a list containing L1[i]/L2[i]"""
#    ratios=[]
#    for index in range(len(L1)):
#        
#        ratios.append(L1[index]/L2[index])
#    return ratios

     
a=[3,5,7,9]
b=[12,15,18,21]
c=[0,0,6,7]
d=['a','b',3,6]
#print(get_ratios(b,a))

#With exceptions
#def get_ratio(L1,L2):
#    
#    """Assumes : L1 and L2 are lists of equal length of numbers.
#    Returns: a list contains L1[i]/L2[i]"""
#    ratios=[]
#    for index in range(len(L1)):
#        
#        try:
#            ratios.append(L1[index]/L2[index])
#        except ZeroDivisionError:
#            ratios.append(float('nan'))
#        except:
#            raise ValueError("get_ratio called with bad arguments")
#        
#    
#    return ratios
#
#print(get_ratio(b,a))
#print(get_ratio(b,c))#zero divistion error
#print(get_ratio(b,d))

#################
#Example for EXception
#test grades of students

test_grades=[[['peter','parker'],[80.0,70.0,85.0]],
             [['bruce','wayne'],[100.0,80.0,74.0]]]

#Create a new class list , with name, grades, and an average

#ASSERTION-Read after all the elements below(because of the scope)
#Defensive programming technique
#Raise and assertion error if it is given an empty list for grades
#otherwise run OK
#Prevent program propagating bad values
def avg_assert(grades):
    assert not len(grades)==0,"No grades Data"
    return sum(grades) 
    
def get_stats(class_list):

    new_stats=[]
    for elt in class_list:
        new_stats.append([elt[0],elt[1],avg_assert(elt[1])])#appending to empty list
    return new_stats
    
def avg(grades):
    return sum(grades)/len(grades)
    
print(get_stats(test_grades))

#modifying avg() to handle zerodivision error
def avg_zero(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print("Warning: no grades data")
        return 0.0
      
     



###What if there is a student in class who didn't show up for any tests

#new list

test_grades_empty=[[['peter','parker'],[80.0,70.0,85.0]],
             [['bruce','wayne'],[100.0,80.0,74.0]],
             [['captain','america'],[8.0,10.0,96.0]],
             [['deadpool'],[]]]
             


print(get_stats(test_grades_empty))



        
