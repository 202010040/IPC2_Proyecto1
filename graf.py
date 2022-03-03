import xml.etree.ElementTree as ET

try:
    xml_file = open("prueba.xml")# Abrir XML
    if xml_file.readable():
        xml_data = ET.fromstring(xml_file.read())
        print (xml_data)
        plantas = xml_data.findall("PLANTA")
        for planta in plantas:
            print ( f"Nombre: {planta.find('NOMBRE').text}")
    else:
        print(False)
except Exception as err:
    print (err)
finally:
    xml_file.close()

#python graf.py