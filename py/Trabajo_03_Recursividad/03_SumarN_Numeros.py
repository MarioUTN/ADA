# -*- coding: utf-8 -*-
"""
Created on Mon May 31 23:26:15 2021

@author: Mario Salazar
"""

from time import time
#3. Realizar un método recursivo que permita sumar los n primeros números.
def SumarNumeros(numero):
    if(numero>0):
        return numero+SumarNumeros(numero-1)
    else:
        return 0
   
numero=int(input("Ingrese un numero: "))
t0=time()
print("Resultado de la suma de 0 a ",numero," es: ",SumarNumeros(numero))
tf=time()
print("Tiempo: {0:f} segundos: ".format(tf-t0))
