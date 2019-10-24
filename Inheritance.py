# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 22:39:09 2019

@author: naveen
"""

#class Animal 
class Animal(object):
    def __init__(self,age):
        self.age=age
        self.name=None
    
    #Getters and setters-they are used for information hiding
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
        
    def set_age(self,newage):
        self.age=newage
    def set_name(self,newname=" "):
        self.name=newname
    def __str__(self):
        return "Animal:"+str(self.name)+":"+str(self.age)
    
a=Animal(3)
#print(a.age)#can access attributes this way but not recommended
#print(a.get_age())#better access method to ouse getters and setters

#Inheritance: Subclass for Animal

class cat(Animal):#Animal is the parent class
    def speak(self):
        print("meow")
    def __str__(self):
        return "cat:"+str(self.name)+":"+str(self.age)
    
#a.set_name("fluffy")
#print(a.get_name())
    
class person(Animal):
    def __init__(self,name,age):
        Animal.__init__(self,age)#call Animal constructor
        self.set_name(name)#call Animal method
        self.friends=[]#Add a new data attribute
    
    def get_friends(self):
        return self.friends
    def add_friends(self,fname):
        if fname not in self.friends:
            self.friends.append(fname)
    def speak(self):
        print "hello"
    def age_diff(self,other):
        diff=(self.age-other.age)
        print(abs(diff),"year difference")
    def __str__(self):
        return "person:"+str(self.name)+":"+str(self.age)
        
#p1=person("Jack",30)
#p2=person("Jill",25)
#print(p1.get_name())
#print(p1.get_age())
#print(p2.get_name())
#print(p2.get_age())
#print(p1)
#p1.speak()
#p1.age_diff(p2)
        
#student class
        
import random

class student(person):
    def __init__(self,name,age,major=None):
        person.__init__(self,name,age)
        self.major=major
    
    def change_major(self,major):
        self.major=major
    def speak(self):
        r=random.random()
        if r<0.25:
            print("i have homework")
        elif 0.5<=r<0.75:
            print("I should eat")
        else:
            print("I am watching tv")
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(self.major)

s1=student("Alice",20,"CS")
s2=student("beth",18)
print(s1)
print(s1.get_name(),"says")
s1.speak()

#class variable
#class variable and their values are shared between all instances of a class
class Rabbit(Animal):
    tag=1
    def __init__(self,age,parent1=None,parent2=None):
        Animal.__init__(self,age)
        self.parent1=parent1
        self.parent2=parent2
        self.rid=Rabbit.tag
        Rabbit.tag+=1
            
    def get_rid(self):
        return str(self.rid).zfill(3)
    def get_parent1(self):
        return self.parent1
    def get_parent2(self):
        return self.parent2
    def __str__(self):
        return "Rabbit:"+str(self.age)+":"+str(self.parent1)+":"+str(self.parent2)
    def __add__(self,other):
        #returning object of the same type as this class
        return Rabbit(0,self,other)
r1=Rabbit(3)
r2=Rabbit(4)
r3=Rabbit(5)
print(r1)
print(r1.get_rid())
print(r2.get_rid())
print(r2.get_parent1())
r4=r1+r2
print("r1",str(r1))
print("r2",r2)
print("r4",str(r4))
print("r4_parent1:",str(r4.get_parent1()))