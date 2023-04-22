# -*- coding: utf-8 -*-
"""
Created on Sat Nov 12 16:36:26 2022

@author: arato
"""

for i in range(1,10):
    for j in range(1,10):
        result=i*j
        if result<10:
            print(result,end='  ')   #1桁でも2桁でも縦横が揃うよう処理
        else:
            print(result,end=' ')
    print()
    