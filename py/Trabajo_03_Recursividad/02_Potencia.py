# -*- coding: utf-8 -*-
"""
Created on Mon May 31 23:20:19 2021

@author: Mario Salazar
"""

from time import time
#2. Realizar un método recursivo que permita calcular la potencia de un número al exponente n.
def Potencia(base,exponente):
    if(exponente>0):
        return base*Potencia(base, exponente-1)
    else:
        return 1
    
a=int(input("Ingrese la base: "))
b=int(input("Ingrese el exponente: "))

t0=time()
print("Resultado: ",Potencia(a,b))
tf=time()
print("Tiempo: {0:f} segundos: ".format(tf-t0))
