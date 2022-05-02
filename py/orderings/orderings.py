# -*- coding: utf-8 -*-
"""
Created on Thu May  6 15:14:44 2021

@author: Mario Salazar
"""
import random as rand
import io as ar
import os as o
from builtins import len
from tkinter import *
from tkinter.ttk import Combobox
from time import time
from tkinter import messagebox as MessageBox

def CrearArchivos():
    archivo = ar.open('Arreglo.txt', 'w')
    archivo.close()

def EscribirArchivo(nf, tam):
    f = ar.open(nf, 'a')
    for i in range(tam):
        numero = rand.randint(0, 25000)
        v = str(numero)
        if (i > tam - 2):
            f.write(v)
        else:
            f.write(v + '\n')
    f.close()


def ArregloArchivo(nf, tam):
    vector = []
    with open(nf, 'r') as f:
        cont = 0;
        for line in f:
            vector.append(int(line.title().strip()))
            cont += 1
            if (cont == tam):
                break;
        f.close()
    return vector


def ImprimirArreglo(arreglo):
    resp = ""
    for i in range(len(arreglo)):
        resp = resp + str(arreglo[i]) + '\t'
    return resp


# Ordenamiento de Burbuja 01
def OrdenamientoBurbuja(Arreglo):
    resp = False
    while (resp == False):
        resp = True
        for i in range(len(Arreglo) - 1):
            if (Arreglo[i] > Arreglo[i + 1]):
                aux = Arreglo[i]
                Arreglo[i] = Arreglo[i + 1]
                Arreglo[i + 1] = aux
                resp = False
    return Arreglo


# Ordenamiento por insercion 02
def OrdenamientoInsercion(Arreglo):
    for i in range(1, len(Arreglo)):
        aux = Arreglo[i]
        a = i - 1
        while (a >= 0):
            if (aux < Arreglo[a]):
                Arreglo[a + 1] = Arreglo[a]
                Arreglo[a] = aux
                a -= 1
            else:
                break
    return Arreglo


# OrdenamientoSeleccion 03
def OrdenamientoSeleccion(Arreglo):
    for i in range(len(Arreglo) - 1, 0, -1):
        posMax = 0
        for j in range(1, i + 1):
            if (Arreglo[j] > Arreglo[posMax]):
                posMax = j
        aux = Arreglo[i]
        Arreglo[i] = Arreglo[posMax]
        Arreglo[posMax] = aux
    return Arreglo


# Ordenamiento Mezcla o Merge Sort 04
def OrdenamientoMergeSort(Arreglo):
    if (len(Arreglo) > 1):
        mitad = len(Arreglo) // 2
        mitadIzquierda = Arreglo[:mitad]
        mitadDerecha = Arreglo[mitad:]
        OrdenamientoMergeSort(mitadIzquierda)
        OrdenamientoMergeSort(mitadDerecha)
        i = 0
        j = 0
        k = 0
        while (i < len(mitadIzquierda) and j < len(mitadDerecha)):
            if (mitadIzquierda[i] < mitadDerecha[j]):
                Arreglo[k] = mitadIzquierda[i]
                i += 1
            else:
                Arreglo[k] = mitadDerecha[j]
                j += 1
            k += 1
        while (i < len(mitadIzquierda)):
            Arreglo[k] = mitadIzquierda[i]
            i += 1
            k += 1
        while (j < len(mitadDerecha)):
            Arreglo[k] = mitadDerecha[j]
            j += 1
            k += 1
    return Arreglo


# Ordenamiento Shell 05
def OrdenamientoShell(Arreglo):
    mitad = len(Arreglo) // 2
    while (mitad > 0):
        for i in range(mitad):
            ReducirBusqueda(Arreglo, i, mitad)
        mitad = mitad // 2
    return Arreglo


def ReducirBusqueda(Arreglo, a, b):
    for i in range(a + b, len(Arreglo), b):
        valor = Arreglo[i]
        posicion = i
        while (posicion >= b and Arreglo[posicion - b] > valor):
            Arreglo[posicion] = Arreglo[posicion - b]
            posicion = posicion - b
        Arreglo[posicion] = valor


# Ordenamiento por QuickSort 06
def OrdenamientoQuickSort(Arreglo):
    QuickSortAuxiliar(Arreglo, 0, len(Arreglo) - 1)
    return Arreglo


def QuickSortAuxiliar(Arreglo, a, b):
    if (a < b):
        partida = Particionar(Arreglo, a, b)
        QuickSortAuxiliar(Arreglo, a, partida - 1)
        QuickSortAuxiliar(Arreglo, partida + 1, b)


def Particionar(Arreglo, a, b):
    pivote = Arreglo[a]
    izq = a + 1
    der = b
    fin = False
    while (not fin):
        while (izq <= der and Arreglo[izq] <= pivote):
            izq += 1
        while (Arreglo[der] >= pivote and der >= izq):
            der -= 1
        if (der < izq):
            fin = True
        else:
            Arreglo[izq], Arreglo[der] = Arreglo[der], Arreglo[izq]
    Arreglo[a], Arreglo[der] = Arreglo[der], Arreglo[a]
    return der


# Ordednamiento RadixSort 07F
def Ordenamiento_RadixSort(Arreglo):
    radix = 10;
    maxLenght = False
    temp, posicion = -1, 1
    while not maxLenght:
        maxLenght = True
        Listas = [list() for _ in range(radix)]
        for i in Arreglo:
            temp = i // posicion
            Listas[temp % radix].append(i)
            if maxLenght and temp > 0:
                maxLenght = False
        a = 0
        for b in range(radix):
            aux = Listas[b]
            for i in aux:
                Arreglo[a] = i
                a += 1
        posicion *= radix
    return Arreglo


# Ordenamiento por Cuentas 08
def OrdenamientoCuentas(Arreglo):
    maximo = max(Arreglo) + 1
    conteo = [0] * maximo
    for n in Arreglo:
        conteo[n] += 1
    i = 0
    for j in range(maximo):
        for k in range(conteo[j]):
            Arreglo[i] = j
            i += 1
    return Arreglo


# Ordenamiento por Casilleros 09
def OrdenamientoBuckSort(Arreglo):
    caja = [0]*(max(Arreglo)+1)
    for i in range(len(Arreglo)):
        caja[Arreglo[i]]=caja[Arreglo[i]]+1
    ouPos=0
    for i in range(len(caja)):
        for j in range(caja[i]):
            Arreglo[ouPos]=i
            ouPos += 1
    return Arreglo


# Ordenamiento por Monticulos 10
def OrdenamientoHeapSort(Arreglo):
    resp = []
    for i in range(len(Arreglo) // 2 - 1, -1, -1):
        Arreglo = Heapyfy(Arreglo, i)
    for i in range(0, len(Arreglo)):
        aux = Arreglo[0]
        Arreglo[0] = Arreglo[len(Arreglo) - 1]
        Arreglo[len(Arreglo) - 1] - aux
        resp.append(aux)
        Arreglo = Arreglo[:len(Arreglo) - 1]
        Arreglo = Heapyfy(Arreglo, 0)
    return resp


def Heapyfy(Arreglo, i):
    if 2 * i + 2 <= len(Arreglo) - 1:
        if Arreglo[2 * i + 1] <= Arreglo[2 * i + 2]:
            min = 2 * i + 1
        else:
            min = 2 * i + 2
        if Arreglo[i] > Arreglo[min]:
            aux = Arreglo[i]
            Arreglo[i] = Arreglo[min]
            Arreglo[min] = aux
            Heapyfy(Arreglo, min)
    elif 2 * i + 1 <= len(Arreglo) - 1:
        if Arreglo[i] > Arreglo[2 * i + 1]:
            aux = Arreglo[i]
            Arreglo[i] = Arreglo[2 * i + 1]
            Arreglo[2 * i + 1] = aux
    return Arreglo


def LlenarArregloDecimales(Arreglo, tam):
    for i in range(tam):
        r = float(rand.random())
        Arreglo.append(r)


def LlenarArregloEnteros(Arreglo, tam):
    for i in range(tam):
        r = rand.randint(0, 100)
        Arreglo.append(r)

def ordenarArreglo():
    t = tam.get()
    d = o.getcwd()
    indice=int(metodos.current())
    BorrarTodo()
    if indice==0 and len(t)>0:
        tamanio0 = int(t)
        vector0 = ArregloArchivo(d + "/Analisis_Algoritmos/ADA/py/Arreglo.txt", tamanio0)
        textArraySinOrdenar.insert('insert', ImprimirArreglo(vector0))
        t0 = time()
        vectorOrdenado0 = OrdenamientoBurbuja(vector0)
        tf0 = time()
        textArrayOrdenado.insert('insert',ImprimirArreglo(vectorOrdenado0))
        tm="Tiempo de ejecución:   {0:f} segundos: ".format(tf0-t0)
        textTE.insert('insert',tm)

    elif indice==1 and len(t)>0:
        tamanio0 = int(t)
        vector0 = ArregloArchivo(d + "/Arreglo.txt", tamanio0)
        textArraySinOrdenar.insert('insert', ImprimirArreglo(vector0))
        t0 = time()
        vectorOrdenado0 = OrdenamientoInsercion(vector0)
        tf0 = time()
        textArrayOrdenado.insert('insert',ImprimirArreglo(vectorOrdenado0))
        tm = "Tiempo de ejecución:   {0:f} segundos: ".format(tf0 - t0)
        textTE.insert('insert', tm)
    elif indice==2 and len(t)>0:
        tamanio0 = int(t)
        vector0 = ArregloArchivo(d + "/Arreglo.txt", tamanio0)
        textArraySinOrdenar.insert('insert', ImprimirArreglo(vector0))
        t0 = time()
        vectorOrdenado0 = OrdenamientoBuckSort(vector0)
        tf0 = time()
        textArrayOrdenado.insert('insert',ImprimirArreglo(vectorOrdenado0))
        tm = "Tiempo de ejecución:   {0:f} segundos: ".format(tf0 - t0)
        textTE.insert('insert', tm)
    elif indice==3 and len(t)>0:
        tamanio0 = int(t)
        vector0 = ArregloArchivo(d + "/Arreglo.txt", tamanio0)
        textArraySinOrdenar.insert('insert', ImprimirArreglo(vector0))
        t0 = time()
        vectorOrdenado0 = OrdenamientoCuentas(vector0)
        tf0 = time()
        textArrayOrdenado.insert('insert',ImprimirArreglo(vectorOrdenado0))
        tm = "Tiempo de ejecución:   {0:f} segundos: ".format(tf0 - t0)
        textTE.insert('insert', tm)
    elif indice==4 and len(t)>0:
        tamanio0 = int(t)
        vector0 = ArregloArchivo(d + "/Arreglo.txt", tamanio0)
        textArraySinOrdenar.insert('insert', ImprimirArreglo(vector0))
        t0 = time()
        vectorOrdenado0 = OrdenamientoMergeSort(vector0)
        tf0 = time()
        textArrayOrdenado.insert('insert',ImprimirArreglo(vectorOrdenado0))
        tm = "Tiempo de ejecución:   {0:f} segundos: ".format(tf0 - t0)
        textTE.insert('insert', tm)
    elif indice==5 and len(t)>0:
        tamanio0 = int(t)
        vector0 = ArregloArchivo(d + "/Arreglo.txt", tamanio0)
        textArraySinOrdenar.insert('insert', ImprimirArreglo(vector0))
        t0 = time()
        vectorOrdenado0 = Ordenamiento_RadixSort(vector0)
        tf0 = time()
        textArrayOrdenado.insert('insert',ImprimirArreglo(vectorOrdenado0))
        tm = "Tiempo de ejecución:   {0:f} segundos: ".format(tf0 - t0)
        textTE.insert('insert', tm)
    elif indice==6 and len(t)>0:
        tamanio0 = int(t)
        vector0 = ArregloArchivo(d + "/Arreglo.txt", tamanio0)
        textArraySinOrdenar.insert('insert', ImprimirArreglo(vector0))
        t0 = time()
        vectorOrdenado0 = OrdenamientoShell(vector0)
        tf0 = time()
        textArrayOrdenado.insert('insert',ImprimirArreglo(vectorOrdenado0))
        tm = "Tiempo de ejecución:   {0:f} segundos: ".format(tf0 - t0)
        textTE.insert('insert', tm)
    elif indice==7 and len(t)>0:
        tamanio0 = int(t)
        vector0 = ArregloArchivo(d + "/Arreglo.txt", tamanio0)
        textArraySinOrdenar.insert('insert', ImprimirArreglo(vector0))
        t0 = time()
        vectorOrdenado0 = OrdenamientoSeleccion(vector0)
        tf0 = time()
        textArrayOrdenado.insert('insert',ImprimirArreglo(vectorOrdenado0))
        tm = "Tiempo de ejecución:   {0:f} segundos: ".format(tf0 - t0)
        textTE.insert('insert', tm)
    elif indice==8 and len(t)>0:
        tamanio0 = int(t)
        vector0 = ArregloArchivo(d + "/Arreglo.txt", tamanio0)
        textArraySinOrdenar.insert('insert', ImprimirArreglo(vector0))
        t0 = time()
        vectorOrdenado0 = OrdenamientoHeapSort(vector0)
        tf0 = time()
        textArrayOrdenado.insert('insert',ImprimirArreglo(vectorOrdenado0))
        tm = "Tiempo de ejecución:   {0:f} segundos: ".format(tf0 - t0)
        textTE.insert('insert', tm)
    elif indice==9 and len(t)>0:
        tamanio0 = int(t)
        vector0 = ArregloArchivo(d + "/Arreglo.txt", tamanio0)
        textArraySinOrdenar.insert('insert', ImprimirArreglo(vector0))
        t0 = time()
        vectorOrdenado0 = OrdenamientoQuickSort(vector0)
        tf0 = time()
        textArrayOrdenado.insert('insert',ImprimirArreglo(vectorOrdenado0))
        tm = "Tiempo de ejecución:   {0:f} segundos: ".format(tf0 - t0)
        textTE.insert('insert', tm)
    else:
        MessageBox.showerror("Ingrese el numero de elementos!!")
        print("Ingrese el numero de elementos!!")


def BorrarTodo():
    textArraySinOrdenar.delete(1.0,END)
    textArrayOrdenado.delete(1.0,END)
    textTE.delete(1.0,END)

ventana=Tk()
ventana.geometry("1000x400")
ventana.title("Análisis de Algoritmos Tiempos estimados de algoritmos de ordenamiento")

LabelTitulo=Label(ventana,text="Análisis de Algoritmos\nProyecto Parcial 1\nTiempos estimados de algoritmos de ordenamiento")
LabelTitulo.place(x=325,y=15)

LabelTamaño=Label(ventana,text="Ingresar el numero de elementos: ")
LabelTamaño.place(x=20,y=100)

tam=Entry(ventana,width=10)
tam.place(x=210,y=100)

LabelMetodos=Label(ventana,text="Elegir el metodo de Ordenamiento: ")
LabelMetodos.place(x=350,y=100)

metodos=Combobox(ventana,values=['Burbuja','Inserción','Casilleros','Cuentas','Mezcla','Radix','Shell','Selección','Montículos','Quicksort'],state='readonly')
metodos.place(x=550,y=100)
metodos.current(0)

LabelAregloOrdenado = Label(ventana, text="Arreglo de numero Enteros Ordenados ")
LabelAregloOrdenado.place(x=20, y=275)

ordenar=Button(ventana,text="Ordenar Arreglo",command=ordenarArreglo)
ordenar.place(x=775,y=97)

borrar=Button(ventana,text="Borrar Todo",command=BorrarTodo)
borrar.place(x=900,y=97)

LabelAregloSinOrdenar=Label(ventana,text="Arreglo de numero Enteros sin ordenar ")
LabelAregloSinOrdenar.place(x=20,y=175)

textArraySinOrdenar=Text(ventana,width=160,height=4,font=("Helvetica",8))
textArraySinOrdenar.place(x=20,y=210)

textArrayOrdenado=Text(ventana,width=160,height=4,font=("Helvetica",8))
textArrayOrdenado.place(x=20,y=310)

textTE=Text(ventana,width=50,height=1,font=("Helvetica",8))
textTE.place(x=500,y=280)


ventana.mainloop()

