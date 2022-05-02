# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 00:16:52 2021

@author: Mario Salazar
"""
# m@r!05@|@z4R-#10
# m@r!05@|@z4R-#10
class Nodo:
    def __init__(self,elemento):
        self.elemento=elemento
        self.Siguiente=None
        
    def __str__(self):
        return str(self.elemento)
    
class ListaEnlazada:
    def __init__(self):
        self.Primero=None
        self.Tam=0
        
    def Agregar(self,elemento):
        MyNodo=Nodo(elemento)
        if(self.Tam==0):
            self.Primero=MyNodo
        else:
            Actual=self.Primero
            while Actual.Siguiente != None :
                Actual=Actual.Siguiente
            Actual.Siguiente=MyNodo
        self.Tam+=1
        return MyNodo
    
    def Eliminar(self,elemento):
        if(self.Tam==0):
            return False
        else:
            Actual=self.Primero
            try:
                while Actual.Siguiente.elemento != elemento:
                    Actual=Actual.Siguiente
                EliminarNodo=Actual.Siguiente
                Actual.Siguiente=EliminarNodo.Siguiente
            except AttributeError:
                return False
        self.Tam-=1
        return EliminarNodo
    
    def Tamanio(self):
        return self.Tam
    
    #10. Realizar un método recursivo que imprima el contenido de una lista enlazada.
    def ImprimirListaEnlazada(self,resp,iterador,b):
        if (iterador < self.Tamanio()):
            resp=str(iterador)+".-  "+str(b)+"\n"
            return resp+self.ImprimirListaEnlazada(resp,iterador+1,b.Siguiente)
        else:
            return ""
        


a=ListaEnlazada()

a.Agregar(1.25)
a.Agregar(28)
a.Agregar(3)
a.Agregar("Mario")
a.Agregar("Juan")
a.Agregar(False)
a.Agregar("Pedro")
a.Agregar(2000)
a.Agregar(0.3)
a.Agregar("Mario")
a.Agregar(-4)
a.Agregar(-555)
a.Agregar(0.0015)
a.Agregar("Luis Perez")
a.Agregar(3.369)
a.Agregar("Maria Jose")
a.Agregar(-89.25)
a.Agregar(True)
a.Agregar("Lizbeth Ordoñez")
a.Agregar(1000000025)
a.Agregar(-89151)
a.Agregar("My Lista Enlazada")
a.Agregar(-44116)
a.Agregar("2/8")

b=a.Primero
#print(a.Eliminar("Mario"))

print(a.ImprimirListaEnlazada("",0,b))