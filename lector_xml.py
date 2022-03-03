import xml.etree.ElementTree as ET
from pisos import PISO
tree = ET.parse('prueba3.xml')
root = tree.getroot()
text = "" #CREA UNA NUEVA CADENA DE TEXTO           
for pisos in root.findall("piso"): #RECORRE TODOS LOS PISOS
    name = pisos.get("nombre") #OBTIENE EL ATRIBUTO NOMBRE
    print (name) 
    for patrones in pisos.findall("patrones"): #POR CADA PISO BUSCA LOS PATRONES
        
        for patron in patrones.findall("patron"): #BUSCA CADA PATRON PORQUE HAY UN NIVEL DE MÁS
         code = patron.get("codigo") #OBTIENE EL CODIGO
         patron0 = patron.text #OBTIENE EL MERO PATRON DE COLORES
         text = str(patron0)
         #Crea una lista
name_list = PISO (3,3,1,1, text.strip())
name_list.mosaico (name_list.filas, name_list.columnas,name_list.codigo)

