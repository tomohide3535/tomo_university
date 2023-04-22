# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 21:36:01 2022

@author: arato
"""

class Car:
    def __init__(self,number,fuel):
        self.number=number
        self.fuel=fuel
    
    def getnumber(self):
        return self.number
    
    def getfuel(self):
        return self.fuel
    
C1=Car(1234,25.5)
n1=C1.getnumber()
f1=C1.getfuel()

C2=Car(2345,30.5)
n2=C2.getnumber()
f2=C2.getfuel()

print("ナンバーは",n1,"ガソリン量は",f1,"です。")
print("ナンバーは",n2,"ガソリン量は",f2,"です。")