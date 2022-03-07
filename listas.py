class Node:
    def __init__(self, valor):
        self.valor = valor
        self.next = None

    def __str__(self):
        return str(self.valor)

class LinkedList :
    def __init__ (self):
        self.primero = None
        self.tamaño = 0

    def añadir (self,valor):
        nodo1 = Node(valor)
        if self.tamaño == 0: #Se verifica si la lista está vacia
            self.primero = nodo1
        else:
            Actual = self.primero
            while Actual.next != None:
                Actual = Actual.next #Mientras el nodo actual sea diferente de null sigue recorriendo la lsita
            Actual.next = nodo1#Añade uno al ultimo
        self.tamaño += 1 #Reyornar es opcional aqui

        return nodo1 

    def eliminar (self, valor):
        if self.tamaño == 0:
            return False
        else:
            Actual = self.primero
            while Actual.next.valor != valor:
                if Actual.next == None:
                   break
                   return False
                else: 
                   Actual = Actual.next
            NodoBorrado = Actual.next
            Actual.next = NodoBorrado.next #Cambia el actual por el siguiente asi lo elimina

        self.tamaño -= 1   

        return NodoBorrado 

    def __len__(self):
        return self.tamaño

    def __str__(self):
        String = "["
        Actual = self.primero
        while Actual != None:
            String += str (Actual)
            if Actual.next != None:
             String += ","
            Actual = Actual.next
        String += "]"
        return String

