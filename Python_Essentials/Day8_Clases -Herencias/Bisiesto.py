# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 15:27:24 2023

@author: myepez
"""

#Determinar si un año es bisiesto
def isYearLeap(year):
    div4=int(year/4)
    if div4*4==year:
        div100=int(year/100)
        if div100*100==year:
            div400=int(year/400)
            if div400*400==year:
                print("El año ",year," es un año bisiesto")
                leap=True
                return leap
            else:
                print("El año ",year," no es un año bisiesto")
                leap=False
                return leap                
        else:
            print("El año ",year," es un año bisiesto")
            leap=True
            return leap
    else:
         print("El año ",year," no es un año bisiesto")
         leap=False
         return leap
            
testData=[1900, 2000, 2016, 1987]
testResults=[False,True,True,False]

for i in range(len(testData)):
    yr=testData[i]
    print(yr," -> ")
    result=isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
                