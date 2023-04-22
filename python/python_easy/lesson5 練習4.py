# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 13:26:16 2022

@author: arato
"""

city=['東京','名古屋','大阪','京都','福岡']
high=[32,28,27,26,27]
low=[25,21,20,19,22]
print("都市のデータは",city,"です。")
print("最高気温のデータは",high,"です。")
print("最低気温のデータは",low,"です。")
for c,h,l in zip(city,high,low):
    print(c,"の最高気温は",h,"最低気温は",l,"です。")