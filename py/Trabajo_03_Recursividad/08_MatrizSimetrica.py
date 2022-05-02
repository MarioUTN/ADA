# -*- coding: utf-8 -*-
"""
Created on Mon May 31 23:53:07 2021

@author: Mario Salazar
"""
from time import time
import random as mario
#8. Realizar un método recursivo que verifique si una matriz es simétrica o no.
def MatrizSimetrica(matriz,fila,col,resp):
    if(resp and fila<len(matriz)):
        if(matriz[fila][col]!=matriz[col][fila] or len(matriz)!=len(matriz[0])):
            resp=False
        if(col==len(matriz[0])-1):
            col=0
            fila+=1
        else:
            col+=1
        return MatrizSimetrica(matriz, fila, col, resp)
    else:
        return resp


def ImprimirMatriz(matriz,fila,col,resp):
    if(col<len(matriz[0]) and fila<len(matriz)):
        resp=str(matriz[fila][col])+"\t"
        if(col==len(matriz[0])-1):
            col=0
            fila+=1
            resp=resp+"\n"
        else:
            col+=1
        return resp+ImprimirMatriz(matriz, fila, col, resp)
    else:
        return ""

def CrearMatriz(matriz,f,c,filas,columnas):
    if(f<=filas-1 and c<=columnas-1):
        if(c==columnas-1):
            matriz.append([])
            c=0;
            f+=1
        else:
            c+=1
        CrearMatriz(matriz,f, c,filas,columnas)     
        
def LlenarMatriz(matriz,f,c,filas,columnas):
    if(f<=filas-1 and c<=columnas-1):
        matriz[f].append(mario.randint(0, 100))
        if(c==columnas-1):
            c=0;
            f+=1
        else:
            c+=1
        LlenarMatriz(matriz,f, c,filas,columnas)
        

n=int(input("Ingrese el valor de n: "))
#matriz=[[-2,1,3],[1,-3,2],[3,2,7]]
matriz=[]
CrearMatriz(matriz, 0, 0, n, n)
LlenarMatriz(matriz, 0, 0, n, n)
print(ImprimirMatriz(matriz, 0, 0, ""))
t0=time()
if(MatrizSimetrica(matriz, 0, 0, True)):
    print("La matris es simetrica!")
else:
    print("La matriz no es simetrica!")
tf=time()
print("Tiempo: {0:f} segundos: ".format(tf-t0))










