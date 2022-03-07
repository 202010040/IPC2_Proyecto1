from listas import LinkedList
import graphviz, pydot
class Matriz:
    def __init__(self,filas,columnas,code): #IMPORTA LO NECESARIO PARA FUNCIONAR
        self.filas = filas
        self.columnas = columnas
        self.code = code
    def crear_matriz (self):
        self.matriz = LinkedList()
        i = 0  #ITERADOR DE FILAS
        j = 0 #ITERADOR DE COLUMNAS
        k = 0 #ITERAODR DE LETRAS 
        while i < self.filas: #RECORRE LAS FILAS, SIEMPRE HAY QUE SER MENOR PUES COMIENZA EN 0
            name = str(i+1)
            name = LinkedList() #CREAR UNA NUEVA LSITA POR CADA FILA
            while j < self.columnas : #RECORRE LAS COLUMNAS, lo mismo que las filas
                letra = str(self.code)[k] #GUARDA LA VARIABLE EN UNA LETRA
                name.añadir(letra) #EN LA LISTA AÑADE EL VALOR DE LA LETRA EN CUESTIÓN
                j +=1
                k +=1
            self.matriz.añadir(name)
            i +=1
            j = 0
    def crar_dot (self):
        dot = graphviz.Digraph(str(self.code), comment='Matriz actual:') #Crear un dot
        i = 0  #ITERADOR DE FILAS
        j = 0 #ITERADOR DE COLUMNAS
        k = 0 #ITERAODR DE LETRAS 
        while i < self.filas: #RECORRE LAS FILAS, SIEMPRE HAY QUE SER MENOR PUES COMIENZA EN 0
            while j < self.columnas : #RECORRE LAS COLUMNAS, lo mismo que las filas
                letra = str(self.code)[k] #GUARDA LA VARIABLE EN UNA LETRA
                dot.node ("x"+letra, letra)
                if j 
                j +=1
                k +=1
            i +=1
            j = 0

class Patron :
    def __init__(self,matriz,nombre):#HAGO UN PISO CON ATRIUTOS DE NOMBRE Y MATRIZ
        self.matriz = matriz
        self.nombre = nombre

class operacion :
    def __init__(self,nombre,costo_volteo,costo_intercambio,patrones):
        self.nombre= nombre
        self.costo_volteo = costo_volteo
        self.costo_intercambio = costo_intercambio
        self_patrones = patrones
    def __str__(self):
        String = ""
        Actual = self.primero
        while Actual != None:
            String += Actual
            if Actual != None:
                String += ", "
                Actual = Actual.next
        print (String)
        return String

