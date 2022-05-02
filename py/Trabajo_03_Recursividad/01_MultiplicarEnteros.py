# -*- coding: utf-8 -*-
"""
Created on Mon May 31 23:14:18 2021

@author: Mario Salazar
"""
from time import time
#1. Realizar un método recursivo que permita multiplicar dos números enteros positivos.
def MultiplicarEnterosPositivos(a,b):
    if(b>0):
        return a+MultiplicarEnterosPositivos(a,b-1)
    else:
        return 0
    
a=int(input("Ingrese el primer numero: "))
b=int(input("Ingrese el segundo numero: "))

t0=time()
print("Resultado: ",MultiplicarEnterosPositivos(a,b))
tf=time()
print("Tiempo: {0:f} segundos: ".format(tf-t0))