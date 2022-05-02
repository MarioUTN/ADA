# -*- coding: utf-8 -*-
"""
Created on Mon May 31 23:39:36 2021

@author: Mario Salazar
"""
from time import time
import random as mario
#4. Realizar un método recursivo que permita sumar los elementos de un arreglo de n datos.
def LlenarArreglo(arreglo,tam):
    if(tam>0):
        arreglo.append(mario.randint(0, 25))
        LlenarArreglo(arreglo, tam-1)
        
def ImprimirArreglo(arreglo,i):
    if(i<len(arreglo)):
        return str(arreglo[i])+"\t"+ImprimirArreglo(arreglo, i+1)
    else:
        return ""

def NumeroMayorArreglo(arreglo,i,maximo):
    if(i<len(arreglo)):
        if(arreglo[i]>maximo):
            maximo=NumeroMayorArreglo(arreglo, i+1, arreglo[i])
        else:
            maximo=NumeroMayorArreglo(arreglo, i+1, maximo)
    return maximo
   
tam=int(input("Ingrese el tamaño del arreglo: "))
arreglo=[]
LlenarArreglo(arreglo,tam)
print(ImprimirArreglo(arreglo,0))
t0=time()
print("El mayor numero del arreglo es: ",NumeroMayorArreglo(arreglo,0,0))
tf=time()
print("Tiempo: {0:f} segundos: ".format(tf-t0))