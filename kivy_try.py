# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:35:54 2019

@author: naveen
"""
import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.uix.label import Label

class myApp(App):
    
    def build(self):
        return Label(text="hello world")

if __name__=='__main__':
    myApp().run()