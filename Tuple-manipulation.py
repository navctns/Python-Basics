# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 00:07:39 2019

@author: naveen
"""

#manipulating tuples
def get_data(aTuple):
    nums=()#defining emply tuples
    words=()
    for t in aTuple:
        nums=nums+(t[0],)
        #concatenating with singleton tuple
        #only add words haven't added before
        if t[1] not in words:
            words=words+ (t[1],)
    min_n=min(nums)
    max_n=max(nums)
    unique_words=len(words)
    return (min_n,max_n,unique_words)
        
test=((1,"a"),(2,"b"),(1,"a"),(7,"b"))
(a,b,c)=get_data(test)
print("a:",a,"b:",b,"c:",c)
            