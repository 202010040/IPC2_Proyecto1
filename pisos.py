from json.tool import main
from listas import LinkedList
matrices = LinkedList () #Crear un listado de matrices
class PISO:
    def __init__(self,filas,columnas,costo_v,costo_i,code,codigo): #IMPORTA LO NECESARIO PARA FUNCIONAR
        self.filas = filas
        self.columnas = columnas
        self.costo_v = costo_v
        self.costo_i = costo_i
        self.code = code
        self.codigo = codigo
    def mosaico (self, filas, columnas,code):
        matriz = str (self.codigo)#Crea la matriz
        matriz = LinkedList()
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
            matriz.añadir(name)
            print (matriz)
            i +=1
            j = 0
        matrices.añadir(matriz) #añade las filas a una matriz
        print (matrices)
