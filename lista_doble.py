from ast import Constant
from cProfile import label
from lib2to3.pgen2.grammar import Grammar
from tkinter.ttk import Style
from turtle import color
import graphviz
from Lista import Lista
import pydot
class lista_doble:
    def __init__(self):
        self.primero = None
        self.ultimo = None
    
    def vacia (self): #Comprueba si la lista está vacia
        if self.primero == None:
            return True
        else:
            return False
    
    def  agregar_primero (self,color,posicion) :
        nuevo = Lista(color,posicion)
        if self.vacia():
            self.primero = self.ultimo = nuevo
        else:
            temp = nuevo
            temp.siguiente =self.primero
            self.primero.anterior = temp
            self.primero = temp
            self.unir()
    
    def agregar_ultimo (self,color,posicion):
        nuevo = Lista(color,posicion)
        if self.vacia():
            self.primero = self.ultimo = nuevo
        else:
            temp = self.ultimo
            self.ultimo = temp.siguiente = nuevo
            self.ultimo.anterior = temp
            self.unir()
    
    def unir (self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero

    def eliminarPrimero (self,color,posicion):
        if self.vacia():
            print ("Lo siento, pero la lista está vacia")
        elif self.primero == self.ultimo:
            self.primero = self.ultimo = None
        else:
            self.primero = self.primero.siguiente
            self.umir()
    def recorrer (self):
        temp = self.primero
        while temp:
            print(temp.color,temp.posicion)
            temp = temp.siguiente
            if temp == self.primero:
                break
    def buscar (self, color,posicion):
        temp = self.primero
        while temp:
            if temp.color == color and temp.posicion == posicion:
                return True
            else:
                temp = temp.siguiente
                if temp == self.primero:
                    return False

    def reporte (self): #ESTO NO SE USA
        temp = self.primero
        text = "digraph  G{\n\n"
        text += "rankdir=LR; \n node[shape=egg,style=filled,color=khaki,fontname=\"Century Gothic\"]; graph [fontname = \"Century Gothic\"];\n"
        text += "labelloc = \"t;\"label = \"Lista\";\n"
        while temp:
            text += "i" + str(temp.color)+"[dir=both label = \"Color = "+str(temp.color)+"\\Posicion = "+str(temp.posicion)+ "\"]"
            text += "i"+str(temp.color)+"-> i"+str(temp.siguiente.color)+"\n"
            text += "i"+ str(temp.color)+"-> i"+str(temp.anterior.color)+"\n"
            temp = temp.siguiente
            if temp != self.primero:
                text += "i" + str(temp.color)+"[dir=both label = \"Color = "+str(temp.color)+"\\Posicion = "+str(temp.posicion)+ "\"]" 
                print (text)
            if temp == self.ultimo:
                text += "i"+str(temp.color)+"-> i"+str(temp.siguiente.color)+"\n"
                text += "i"+ str(temp.color)+"-> i"+str(temp.anterior.color)+"\n"
                break
        return text

    def reportar (self): #ESTO TAMPOCO SE USA
        contenido = str(self.reporte())+"\n}"
        f = open ("ejemplo.txt","w")
        f.write(contenido)
        f.close()
        print ("listo")
  
    def reporte2_1 (self):
        f = graphviz.Digraph("G",filename="Ejemplo.dot",format='dot',node_attr= {'shape': 'record', 'height': '1'},edge_attr={'style':'dashed'},renderer="dot",directory='imagenes')
        f.graph_attr["rankdir"]="LR"#DERECHA A IZQUIERDA
        f.attr(rank = "same")#MISMO RANGO
        temp = self.primero
        while temp:
            if temp == self.ultimo:
                break
            else:
                if temp.color== "blanco":
                     f.node(str(temp.color)+ ", " + str(temp.posicion))
                elif temp.color== "negro":
                     f.node(str(temp.color)+ ", " + str(temp.posicion), style="filled", color= "black", fontcolor='white')
                if temp.siguiente.color== "blanco":
                     f.node(str(temp.siguiente.color)+ ", " + str(temp.siguiente.posicion))
                elif temp.siguiente.color== "negro":
                     f.node(str(temp.siguiente.color)+ ", " + str(temp.siguiente.posicion), style="filled", color= "black",fontcolor='white')
                f.edge (str(temp.color)+ ", " + str(temp.posicion) , str(temp.siguiente.color)+ ", " + str(temp.siguiente.posicion))
                f.edge (str(temp.siguiente.color)+ ", " + str(temp.siguiente.posicion),str(temp.color)+ ", " + str(temp.posicion))
                temp = temp.siguiente
        return (f)

    def reportar2 (self,nombre): #CREA UN REPORTE DE SALIDA
        x = self.reporte2_1().source
        graf = pydot.graph_from_dot_data(x)
        name = nombre+".png"
        graf[0].write_png(name)
        