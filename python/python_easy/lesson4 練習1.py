# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 21:52:08 2022

@author: arato
"""

print("1から10までの偶数を表示します。")

for i in range(1,11,1):
    #停止値を必要な数+1で設定する。この場合は10まで必要なため、11を停止値にする。
    if i%2==0 :
        print(i)