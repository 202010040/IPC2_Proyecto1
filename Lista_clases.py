from temp import mosaico_t, patron_t, piso_t
import graphviz
import pydot
class patron_list:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia (self):
        if self.primero == None:
            return True
        else:
            return False

    def unir(self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero

    def añadir (self,codigo,texto):
         nuevo = patron_t (codigo,texto)
         if self.vacia():
            self.primero = self.ultimo = nuevo
         else:
            temp = self.ultimo
            self.ultimo = temp.siguiente = nuevo
            self.ultimo.anterior = temp
            self.unir()

    def recorrer (self):
        temp = self.primero
        while temp:
            print(temp.codigo,temp.texto)
            temp = temp.siguiente
            if temp == self.primero:
                break

class pisos_list:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia (self):
        if self.primero == None:
            return True
        else:
            return False

    def unir(self):
        if self.primero != None:
            self.primero.anterior = self.ultimo
            self.ultimo.siguiente = self.primero

    def añadir (self,nombre,rows,col,vol,intercambio,patrones):
        nuevo = piso_t (nombre,rows,col,vol,intercambio,patrones)
        if self.vacia():
            self.primero = self.ultimo = nuevo
        else:
            temp = self.ultimo
            self.ultimo = temp.siguiente = nuevo
            self.ultimo.anterior = temp
            self.unir()

    def recorrer (self):
        temp = self.primero
        while temp:
            print(temp.nombre,temp.rows,temp.col,temp.vol,temp.intercambio)
            temp0 = temp.patrones.primero

            while temp0:
                print (temp0.codigo,temp0.texto)
                temp0=temp0.siguiente
                if temp0 == temp.patrones.primero:
                     break

            temp = temp.siguiente
            if temp == self.primero:
                break

    def mosaico1(self):
        temp = self.primero
        while temp:
            temp0 = temp.patrones.primero

            while temp0:
                print(temp0.texto)
                self.mosaico2(temp.rows,temp.col,temp0.texto,temp.nombre + temp0.codigo)
                temp0=temp0.siguiente
                if temp0 == temp.patrones.primero:
                     break

            temp = temp.siguiente
            if temp == self.primero:
                break
            

    def mosaico2 (self, filas, columnas,code,nombre):
        i = 0  #ITERADOR DE FILAS
        j = 0 #ITERADOR DE COLUMNAS
        k = 0 #ITERAODR DE LETRAS 
        while i < filas: #RECORRE LAS FILAS, SIEMPRE HAY QUE SER MENOR PUES COMIENZA EN 0
            name = mosaico_list() #CREAR UNA NUEVA LSITA POR CADA FILA
            while j < columnas : #RECORRE LAS COLUMNAS, lo mismo que las filas
                if k < len(str(code)):
                    letra = str(code)[k] #GUARDA LA VARIABLE EN UNA LETRA
                name.agregar_ultimo(letra," "+ str(i+1)+str(j+1)) #EN LA LISTA AÑADE EL VALOR DE LA LETRA EN CUESTIÓN
                j +=1
                k +=1
                name.reportar(nombre + "-" + str(i))
            i +=1
            j = 0

    def html (self):
        texto = """<DOCTYPE html>
                    <html>
                     <head>
                         <link href="estilo.css" rel="stylesheet" type="text/css">
                     </head>
                    <body> 
                    <h3>Bienvenido al robot</h3>"""

        temp = self.primero
        while temp :
            temp0 = temp.patrones.primero
            texto += """<h1>Para el """
            texto += temp.nombre
            texto += " El costo por volteo es de: </h1>"""

        texto += """</body>
                    </html>"""

class mosaico_list:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia (self): #Comprueba si la lista está vacia
        if self.primero == None:
            return True
        else:
            return False
    
    def agregar_ultimo (self,color,posicion):
        nuevo = mosaico_t(color,posicion)
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
  
    def reporte (self):
        f = graphviz.Digraph("G",filename="Ejemplo.dot",format='dot',node_attr= {'shape': 'record', 'height': '1'},edge_attr={'style':'dashed'},renderer="dot",directory='imagenes')
        f.graph_attr["rankdir"]="LR"#DERECHA A IZQUIERDA
        f.attr(rank = "same")#MISMO RANGO
        temp = self.primero
        while temp:
            if temp == self.ultimo:
                break
            else:
                if temp.color== "W":
                     f.node(str(temp.color)+ ", " + str(temp.posicion))
                elif temp.color== "B":
                     f.node(str(temp.color)+ ", " + str(temp.posicion), style="filled", color= "black", fontcolor='white')
                if temp.siguiente.color== "W":
                     f.node(str(temp.siguiente.color)+ ", " + str(temp.siguiente.posicion))
                elif temp.siguiente.color== "B":
                     f.node(str(temp.siguiente.color)+ ", " + str(temp.siguiente.posicion), style="filled", color= "black",fontcolor='white')
                f.edge (str(temp.color)+ ", " + str(temp.posicion) , str(temp.siguiente.color)+ ", " + str(temp.siguiente.posicion))
                f.edge (str(temp.siguiente.color)+ ", " + str(temp.siguiente.posicion),str(temp.color)+ ", " + str(temp.posicion))
                temp = temp.siguiente
        return (f)

    def reportar (self,nombre): #CREA UN REPORTE DE SALIDA
        x = self.reporte().source
        graf = pydot.graph_from_dot_data(x)
        name = nombre+".png"
        graf[0].write_png(name)
        