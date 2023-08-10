# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False

    return True
#print (isPrime(7))

for i in range(1, 20):
	if isPrime(i + 1):
			print(i + 1,end=" ")
print()

