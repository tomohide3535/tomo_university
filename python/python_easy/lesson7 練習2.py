# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 12:20:33 2022

@author: arato
"""
def rpstr(num,str="*"):
    print(str*num)
    
s=input("文字列を入力して下さい。")
n=int(input("個数を入力して下さい。"))

print("文字列あり---")
rpstr(n,s)

print("文字列なし---")
rpstr(n)