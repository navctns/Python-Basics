## -*- coding: utf-8 -*-
#"""
#Created on Sat Jun  1 00:37:07 2019
#
#@author: naveen
#"""
#
##lists
#a_list=[]#empty list
#L=[2,'a',4,[1,2]]#Element of a list can be another list
#print("length of list:",len(L))
#print(L[0])
#print(L[2]+1)
#print(L[3])
##print(L[4]) Gives an error, list index out of range
#i=3
#print(L[i-2])
## list is mutable
#L=[2,1,3]
#L[1]=5
#print(L)
#
###iterating over a list###
##finding sum of elements in list
#total=0
#for i in range(len(L)):
#    total+=L[i]
#print total
#
##another methon, pythonic
#total=0
#for i in L:
#    total+=i
#print total
##operations on lists
##add elements to list using append()
#L=[2,1,3]
#L.append(5)
#print(L)
#L.extend([7,9])#extending list with other list
#print(L)
##Deleting elements ,at a specific index
#del(L[1])
#print L
#L.append(5)
#print L
#L.remove(5)#removes a specific elements, if element occurs multiple times, removes first occurence
#print L
#L.pop()
#print L
#a=L.pop()
#print a
###Convert a list into a string and back

#s="I<3 cs"#is a string
#list(s)#converting string into a list
#print(list(s))
#print(s.split('<'))#not all the characters in the string are seperated, it is splitted using a single element
#L=['a','b','c']
#print(''.join(L))#converting list into a string
#print('_'.join(L))#gives a different result, all selments are seperated by underscores

###other operations#####
#sort,sorted,reverse
#L=[9,6,0,3]
#print(sorted(L))#returns sorted list, doesn't mutate L
#L.sort()#Lis sorted, mutates L
#print(L)
#L.reverse()#sort L in reverse order, mutates L
#print(L)

####ALIASES########
#a=1
#b=a
#print(a)
#print(b)
#
##side effect when appending
#warm=['red','yellow','orange']
#hot=warm
#hot.append('pink')
#print(warm)
#print(hot)
##both gives the same result, because both binded to the same object

#CLONINT A LIST
#MAKING A DUPLICATE
#cool=['blue','green','grey']
#chill=cool[:]#cloning, or duplicating cool
#chill.append('black')
#print("chill:",chill)
#print("cool:",cool)

##when sorting lists
#warm=['red','yellow','orange']
#print(warm)
#sorted_warm=warm.sort()#doesnt return anything
#print(warm)
#print(sorted_warm)
#
#cool=['grey','green','blue']
#sorted_cool=sorted(cool)
#print("cool:",cool)
#print("sorted cool:",sorted_cool)

##nested lists still have this side effects
#warm=['yellow','orange']
#hot=['red']
#bright_colors=[warm]
#bright_colors.append(hot)
#print(bright_colors)
#hot.append('pink')
#print hot
#print bright_colors

#Mutation and iteration:
 #avoid mutating list as you are iterating over it
def remove_dups(l1,l2):
    for e in l1:
        if e in l2:
            l1.remove(e)
l1=[1,2,3,4]
l2=[1,2,5,6]
remove_dups(l1,l2)
print l1
print l2
#her 2 still ramains in l1,
#python uses an internal counter to keep track of index it is in the loop
#mutating changes the list length but python doesn't update the counter
#thus loop never sees element 2

#solution to that, is ot duplicate the list
def remove_dups_sol(l1,l2):
    l11=l1[:]#making a copy of l1 and iterating over it
    for e in l11:
        if e in l2:
            l1.remove(e)

remove_dups_sol(l1,l2)
print l1
print l2