# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 01:16:36 2021

@author: Chema
"""

lista = [3, 4, 8, 5, 5, 22, 13]

def primos(x):
	
	for i in range(2,x):
		if x % i == 0:
			return False
	return True


primos = list(filter(primos, lista))
print(f'Los números primos dentro de la lista son {primos}')

        
