# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 18:42:11 2022

@author: arato
"""

class Car:
    
    def getnumber(self):
        return self.number
    
    def getfuel(self):
        return self.fuel
    
C1=Car()
C1.number=1234
C1.fuel=25.5
n1=C1.getnumber()
f1=C1.getfuel()

C2=Car()
C2.number=23345
C2.fuel=30.5
n2=C2.getnumber()
f2=C2.getfuel()

print("ナンバーは",n1,"ガソリン量は",f1,"です。")
print("ナンバーは",n2,"ガソリン量は",f2,"です。")