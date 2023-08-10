# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:15:37 2023

@author: myepez
"""

try:
    y=1/0

except ZeroDivisionError:
    print("Zero Division")
        
except ArithmeticError:
    print("Arithmetic problem")

except:
    print("Error")
    
print("THE END")
        