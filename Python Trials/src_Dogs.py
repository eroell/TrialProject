#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:28:30 2021

@author: eljas
"""

class Dog:
    typ = "canine"
    def __init__(self, name):
        self.n = name
        self.tricks = []
        
    def add_tricks(self,trick):
        self.tricks.append(trick)
        
        
class BorderCollie(Dog):
    rasse = "Border Collie"
    
    def __init__(self,name):
        super().__init__(name)
    