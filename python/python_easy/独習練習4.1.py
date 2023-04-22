# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 23:26:22 2022

@author: arato
"""

n=int(input('点数を入力してください'))

if n>=90:
    print('優')
    print(n)
elif n>=70:
    print('良')
    print(n)
elif n>=50:
    print('可')
    print(n)
else:
    print('不可')
    print(n)
    
    
#print(n)は、いらない