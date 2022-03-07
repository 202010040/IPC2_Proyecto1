class patron_t:
    def __init__(self,codigo,texto):
        self.codigo = codigo
        self.texto = texto
        self.siguiente = None
        self.anterior = None

class piso_t:
    def __init__(self, nombre,rows,col,vol,intercambio,patrones):
        self.nombre = nombre
        self.rows = rows
        self.col = col
        self.vol = vol
        self.intercambio = intercambio
        self.patrones = patrones
        self.siguiente = None
        self.anterior = None

class mosaico_t :
    def __init__(self,color,posicion):
        self.posicion = posicion
        self.color =color
        self.siguiente = None
        self.anterior = None