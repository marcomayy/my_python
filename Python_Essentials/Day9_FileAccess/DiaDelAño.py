# -*- coding: utf-8 -*-
"""
Created on Sun Aug  6 18:42:10 2023

@author: myepez
"""
#Calcular el día del año (día juliano)
def dayOfYear(year,month,day):
    #print("Mes del año: ",month)
    sumdays=0
    for i in range(1,month):
        nmdays=daysInMonth(i,year)
        sumdays=sumdays+nmdays
    #print("Total días has fin de mes anterior: ",sumdays)
    sumdays=sumdays+day
    #print("Total de días: ",sumdays)
    return sumdays        
    
def daysInMonth(month,year):
    m31d=[1,3,5,7,8,10,12]
    bisiesto=isYearLeap(year)
    if month in m31d:
        #print(month," tiene 31 días")
        d=31
    elif month==2:
        if bisiesto==False:
            #print(month," tiene 28 días")
            d=28              
        else:
            #print(month," tiene 29 días")
            d=29
    else:
        m30d=[4,6,9,11]
        if month in m30d:
            #print(month," tiene 30 días")
            d=30
        else:
            print("Mes no existe")
            d=0
    return d

def isYearLeap(year):
    div4=int(year/4)
    if div4*4==year:
        div100=int(year/100)
        if div100*100==year:
            div400=int(year/400)
            if div400*400==year:
                #print("El año ",year," es un año bisiesto")
                leap=True
                return leap
            else:
                #print("El año ",year," no es un año bisiesto")
                leap=False
                return leap                
        else:
            #print("El año ",year," es un año bisiesto")
            leap=True
            return leap
    else:
         #print("El año ",year," no es un año bisiesto")
         leap=False
         return leap
     
print("Corresponde al día del año:")
print(dayOfYear(2000,12,31))