class mesa:

    __longitud = 0
    __ancho = 0

    def __init__(self, l, a):
        self.__longitud = l
        self.__ancho = a

    def obtenerLongitud(self):
        return self.__longitud

    longitud = property(obtenerLongitud, doc= ' longitud de la mesa')

m = mesa(21,34)
print(m.longitud)