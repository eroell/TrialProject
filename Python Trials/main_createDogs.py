#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:29:22 2021

@author: eljas
"""

# import src_Dogs

# jolie = src_Dogs.Dog("Jolie")

# print(jolie.typ)
# print(jolie.n)

# jackie = src_Dogs.BorderCollie("Jackie")
# print(jackie.typ)
# print(jackie.n)
# print(jackie.rasse)
# jackie.add_tricks("platz")
# print(jackie.tricks  )

import numpy as np
import matplotlib.pyplot as plt

# np.var: teilt durch n
# np.cov: teilt durch n-1, kann mit bias = true durch n teilen
# np.corrcoef: teilt durch n
a = np.array([[1,2,3,4],[5,5.4,6,7.9]])
plt.plot(a[0],a[1])
print(a.shape)

print(np.corrcoef(a))
print(np.cov(a[0],a[1], bias = True))

print(np.cov(a[0],a[1], bias = True)[0,1] / (np.sqrt(np.var(a[0])) * np.sqrt(np.var(a[1]))) )

print("---------------------")

print(np.cov(a[0],a[1]))
print(np.var(a[0]))
