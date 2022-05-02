# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 00:10:03 2021
@author: Mario Salazar
"""

from time import time
import random as mario
#9. Realizar un método recursivo que calcule la matriz transpuesta de una matriz de orden n*m
def MatrizTranspuesta(matriz,transpuesta,fila,col):
    if(fila<len(matriz) and col<len(matriz[0])):
        transpuesta[col].append(matriz[fila][col])
        if(col==len(matriz[0])-1):
            col=0
            fila+=1
        else:
            col+=1
        return MatrizTranspuesta(matriz, transpuesta, fila, col)
    return transpuesta

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
        

filas=int(input("Ingrese el numero de filas: "))
columnas=int(input("Ingrese el numero de columnas: "))
matriz=[]
transpuesta=[]
CrearMatriz(transpuesta, 0, 0, columnas, filas)
CrearMatriz(matriz, 0, 0, filas, columnas)
LlenarMatriz(matriz, 0, 0, filas, columnas)
print(ImprimirMatriz(matriz, 0, 0, ""))
t0=time()
resp=MatrizTranspuesta(matriz, transpuesta, 0, 0)
tf=time()
print("Tiempo: {0:f} segundos: ".format(tf-t0))
print(ImprimirMatriz(resp, 0, 0, ""))