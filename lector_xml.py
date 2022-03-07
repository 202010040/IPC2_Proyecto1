import xml.etree.ElementTree as ET
from listas import LinkedList
from pisos import PISO
from matriz import Matriz,Patron,operacion
tree = ET.parse('prueba3.xml')
root = tree.getroot()
text = "" #CREA UNA NUEVA CADENA DE TEXTO        
rows = 0 #NUMERO DE FILAS
col = 0 #NUMERO DE COMLUMNAS   
costo_volteo = 0
costo_intercambio = 0


operacionlist = LinkedList()#Listado de pisos

for pisos in root.findall("piso"): #RECORRE TODOS LOS PISOS
    name = pisos.get("nombre") #OBTIENE EL ATRIBUTO NOMBRE
    patronlist = LinkedList() #Listado de patrones
    for filas in pisos.findall("R"):#OBTIENE LAS FILAS
        rows = int (filas.text)
    for columnas in pisos.findall("C"):#OBTIENE LAS COLUMNAS
        col = int (columnas.text)
    for volteos in pisos.findall("F"):#OBIENE EL COSTO DE VOLTEO
        costo_volteo = int (volteos.text)
    for intercambios in pisos.findall("S"):#OBTIENE EL COSTO DE INTERCAMBIO
        costo_intercambio = int (intercambios.text)
    for patrones in pisos.findall("patrones"): #POR CADA PISO BUSCA LOS PATRONES 
        for patron in patrones.findall("patron"): #BUSCA CADA PATRON PORQUE HAY UN NIVEL DE MÁS
         code = patron.get("codigo") #OBTIENE EL CODIGO
         patron0 = patron.text #OBTIENE EL MERO PATRON DE COLORES
         text = str(patron0)
         Matriz1 = Matriz (rows,col,text.strip())#Crea una lista de listas
         Matriz1.crear_matriz()
         Patron0 = Patron(Matriz1,code)#Guarda la matriz y un nombre de patron
         patronlist.añadir(Patron0)
         #Crea una lista
    Operacion0 = operacion(name,costo_volteo,costo_intercambio,patronlist)#Guarda los pisos iniciale y finales, los costos y demas
    operacionlist.añadir(Operacion0)


#name_list = PISO (rows,col,costo_volteo,costo_intercambio, text.strip(),code)
#name_list.mosaico (name_list.filas, name_list.columnas,name_list.codigo)

