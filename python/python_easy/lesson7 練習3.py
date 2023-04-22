# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:27:22 2022

@author: arato
"""

def makex(x):
    while True:
        yield x
        x=x+1
        
start=int(input("開始値（整数）を入力してください。"))
end=int(input("停止値（整数）を入力してください。"))

for n in makex(start):
    if n>=end:
        break
    print(n)