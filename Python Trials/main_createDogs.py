#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:29:22 2021

@author: eljas
"""

import src_Dogs

jolie = src_Dogs.Dog("Jolie")

print(jolie.typ)
print(jolie.n)

jackie = src_Dogs.BorderCollie("Jackie")
print(jackie.typ)
print(jackie.n)
print(jackie.rasse)
jackie.add_tricks("platz")
print(jackie.tricks  )