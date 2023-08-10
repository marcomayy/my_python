# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 20:55:41 2019

@author: CEC
"""

def is_prime(x):
    if x < 2:
       
        return False
    elif x == 2:
        
        return True  
    for n in range(2, x):
        if x % n ==0:
            return False
    return True
"""
w=is_prime()
print(w)
"""
for i in range(1, 20):
	if is_prime(i+1):
			print(i + 1, end=" ")
print()
