# -*- coding: utf-8 -*-
"""
Created on Mon May 31 23:42:38 2021

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

def ArregloA_ContenidoB(A,B,a,b,cont):
    if(a<len(A) and b<len(B) and len(A)<=len(B)):
        if(A[a] == B[b]):
            a+=1
            b=0
            cont+=1
        else:
            b+=1
        return ArregloA_ContenidoB(A, B, a, b, cont)
    else:
        return cont
   
A=[9,4,5,6,7,7]
B=[1,2,3,4,5,6,7,8,10]
print(ImprimirArreglo(A,0))
print(ImprimirArreglo(B,0))
t0=time()
if(ArregloA_ContenidoB(A, B, 0, 0, 0)!=len(A)):
    print("Arreglo A no esta contenido en el arreglo B")
else:
    print("Arreglo A si esta contenido en el arreglo B")
    
tf=time()
print("Tiempo: {0:f} segundos: ".format(tf-t0))