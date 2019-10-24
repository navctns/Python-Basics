# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 20:35:57 2019

@author: naveen
"""

#RECURSION AND DICTIONARIES

#RECURSION
#Recurstion is a process of repeating items in a self similar way
#Algorithamically: A way to design solutions to problems. By divide-and-conquer or 
#decrease and conquer
#semantically-A programming technique where a function calls itself

#MUltiplication, iteration solution
# a*b is equavalent to "add a to itself b times"
#a+a+a+...+a

def mult_iter(a,b):
    i=b#since b times a is a*b
    res=0
    while i>0:
        res+=a
        i-=1
    return res
    
print(mult_iter(7,5))

#Recursive step
def mult_recur(a,b):
    if(b==1): # the base case
        return a
    else: #recursive step
        return a+a*(b-1)

#print(mult_recur(8,9))

####FACTORIALS########
def factorial_iter(n):
    if n==1:
        return 1
    else:
        prod=1
        for i in range(1,n+1):
            prod*=i
        return prod
        
#print(factorial_iter(5))

##Factorial recursive solution
def factorial_recur(n):
    if n==1:
        return 1
    else:
        
        return n*factorial_recur(n-1) 

#print(factorial_recur(6))

#######################
####The TOWER OH HANOI PROBLEM ##########
def printMove(fr,to):
    print("move from",str(fr)+'to'+str(to))
    
def Towers(n,fr,to,spare):
    if n==1:
        printMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
###Recursion with multiple base cases

def fib(x):
    """assumes x an int>=0 returns fibonacci of x"""
    if x==0 or x==1:
            return 1
    else:
        return fib(x-1)+fib(x-2)
        
#print(fib(5))

###PALINDROME#########
def isPalindrome(s):
    
    def toChars(s):
        s= s.lower()
        ans= ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans=ans+c
        return ans
    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])
            
    return isPal(toChars(s))

print(isPalindrome('asksar'))

####Dictionaries########
#How to store students info
#names=['Ana','John','Denise','Katy']
#grade=['B','A+','A','A']
#course=[2.00,6.0001,20.002,9.01]
#
#def get_grade(student,name_list,grade_list,course_list):
#    i=name_list.index(student)
#    grade=grade_list[i]
#    course=course_list[i]
#    return(course,grade)
#
##print(get_grade(names,grade,course))
##Code should be altered
#
##defining it as a dictionary
#
#grades={'Ana':'B','John':'A+','Denise':'A','Katy':'A'}
#
#print(grades['John'])
##print(grades['sylvan'])
#grades['sylvan']='A'
#print(grades['sylvan'])
#del(grades['Ana'])
#print(grades)
####CREATING A DICTIONARY ########
##Repeatatoin of words in song lyrics
#
she_loves_you = ['she', 'loves', 'you', 'yeah', 'yeah', 
'yeah','she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',

'you', 'think', "you've", 'lost', 'your', 'love',
'well', 'i', 'saw', 'her', 'yesterday-yi-yay',
"it's", 'you', "she's", 'thinking', 'of',
'and', 'she', 'told', 'me', 'what', 'to', 'say-yi-yay',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'she', 'said', 'you', 'hurt', 'her', 'so',
'she', 'almost', 'lost', 'her', 'mind',
'and', 'now', 'she', 'says', 'she', 'knows',
"you're", 'not', 'the', 'hurting', 'kind',

'she', 'says', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',

'you', 'know', "it's", 'up', 'to', 'you',
'i', 'think', "it's", 'only', 'fair',
'pride', 'can', 'hurt', 'you', 'too',
'pologize', 'to', 'her',

'Because', 'she', 'loves', 'you',
'and', 'you', 'know', 'that', "can't", 'be', 'bad',
'Yes', 'she', 'loves', 'you',
'and', 'you', 'know', 'you', 'should', 'be', 'glad',

'oo', 'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'she', 'loves', 'you', 'yeah', 'yeah', 'yeah',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'with', 'a', 'love', 'like', 'that',
'you', 'know', 'you', 'should', 'be', 'glad',
'yeah', 'yeah', 'yeah',
'yeah', 'yeah', 'yeah', 'yeah'
]

#song_lyrics="""Hey, I was doing just fine before I met you
#I drink too much and that's an issue
#But I'm OK
#Hey, you tell your friends it was nice to meet them
#But I hope I never see them
#Again
#
#I know it breaks your heart
#Moved to the city in a broke-down car
#And four years, no calls
#Now you're looking pretty in a hotel bar
#And I, I, I, I, I can't stop
#No, I, I, I, I, I can't stop
#
#So, baby, pull me closer
#In the back seat of your Rover
#That I know you can't afford
#Bite that tattoo on your shoulder
#Pull the sheets right off the corner
#Of that mattress that you stole
#From your roommate back in Boulder
#We ain't ever getting older
#
#We ain't ever getting older
#We ain't ever getting older
#
#You look as good as the day I met you
#I forget just why I left you,
#I was insane
#Stay and play that Blink-182 song
#That we beat to death in Tucson
#OK
#
#I know it breaks your heart
#Moved to the city in a broke-down car
#And four years, no call
#Now I'm looking pretty in a hotel bar
#And I, I, I, I, I can't stop
#No, I, I, I, I, I can't stop
#
#So, baby, pull me closer
#In the back seat of your Rover
#That I know you can't afford
#Bite that tattoo on your shoulder
#Pull the sheets right off the corner
#Of that mattress that you stole
#From your roommate back in Boulder
#We ain't ever getting older
#
#We ain't ever getting older
#We ain't ever getting older
#
#So, baby, pull me closer
#In the back seat of your Rover
#That I know you can't afford
#Bite that tattoo on your shoulder
#Pull the sheets right off the corner
#Of that mattress that you stole
#From your roommate back in Boulder
#We ain't ever getting older
#
#We ain't ever getting older
#No, we ain't ever getting older
#We ain't ever getting older
#No, we ain't ever getting older
#We ain't ever getting older
#We ain't ever getting older
#We ain't ever getting older
#No, we ain't ever getting older
#
#We ain't ever getting older
#No, we ain't ever getting older
#"""
#
#
#
def lyrics_to_frequencies(lyrics):
    myDict={}
    for word in lyrics:
        if word in myDict:
            myDict[word]+=1
        else:
            myDict[word]=1
            
    return myDict

print(lyrics_to_frequencies(she_loves_you))

#finding common words
def most_common_words(freqs):
    values=freqs.values()
    best=max(values)
    words=[]
    for k in freqs:
        if freqs[k]==best:
            words.append(k)
    return (words,best)
print(most_common_words(lyrics_to_frequencies(she_loves_you)))
beatles=lyrics_to_frequencies(she_loves_you)
#
def words_often(freqs,min_times):
    result=[]
    done=False
    while not done:
        temp=most_common_words(freqs)
        if temp[1]>=min_times:
            result.append(temp)
            for w in temp[0]:#deleting the word used form freq
                del(freqs[w])
        else:
            done=True
    return result
print(words_often(beatles,5))
    
##fibonacci-efficient
def fib_efficient(n,d):
    if n in d:
        return d[n]
    else:
        ans=fib_efficient(n-1,d)+fib_efficient(n-2,d)
        d[n]=ans
        return ans
d={1:1 , 2:2}
print(fib_efficient(7,d))





