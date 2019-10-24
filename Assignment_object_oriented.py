# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:45:57 2019

@author: naveen
"""

class NewsStory(object):
    
    def __init__(self,guid,title,description,link,pubdate):
        self.guid=guid
        self.title=title
        self.description=description
        self.link=link
        self.pubdate=pubdate
    #methods
    def get_guid(self):
        
    