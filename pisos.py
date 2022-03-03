from main import LinkedList
class PISO:
    def __init__(self,filas,columnas,costo_v,costo_i,codigo): #IMPORTA LO NECESARIO PARA FUNCIONAR
        self.filas = filas
        self.columnas = columnas
        self.costo_v = costo_v
        self.costo_i = costo_i
        self.codigo = codigo
    def mosaico (self, filas, columnas,codigo):
        i = 0  #ITERADOR DE FILAS
        j = 0 #ITERADOR DE COLUMNAS
        k = 0 #ITERAODR DE LETRAS (NO SE SI SEA NECESARIO)
        while i < self.filas: #RECORRE LAS FILAS, SIEMPRE HAY QUE SER MENOR PUES COMIENZA EN 0
            name = str(i+1)
            name = LinkedList() #CREAR UNA NUEVA LSITA POR CADA FILA
            while j < self.columnas : #RECORRE LAS COLUMNAS, lo mismo que las filas
                letra = str(self.codigo)[k] #GUARDA LA VARIABLE EN UNA LETRA
                name.añadir(letra) #EN LA LISTA AÑADE EL VALOR DE LA LETRA EN CUESTIÓN
                j +=1
                k +=1
            print (name) #IMPRIME LA FILA
            i +=1
            j = 0
        print (True)
