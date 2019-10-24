# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:01:32 2019

@author: naveen
"""

#Understanding program efficiency part 2

#Bisection search
def bisect_search(L,e):
    if L==[]:
        return False
    elif len(L)==1:#these are basic block of recursion
        return L[0]==e
    else:
        half=len(L)//2
        if L[half]>e:
            return bisect_search(L[:half],e)
        else:
            return bisect_search(L[half:],e)

L=[1,5,7,34,44,55,65,78,98,110]
print bisect_search(L,3)

#Implementation 2- using pointers
def bisect_search2(L,e):
    def bisect_search_helper(L,e,low,high):
        if high==low:
            return L[low]==e
        mid=(low+high)//2
        if L[mid]==e:
            return True
        elif L[mid]>e:
            if low==mid:
                return False
            else:
                return bisect_search_helper(L,e,low,mid-1)
        else:
            return bisect_search_helper(L,e,mid+1,high)
    if len(L)==0:
        return False
    else:
        return bisect_search_helper(L,e,0,len(L)-1)

print bisect_search2(L,55)