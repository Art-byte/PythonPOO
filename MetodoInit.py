class Rectangulo:

    __area = 0
    __perimetro = 0

    def __init__(self, a, b):
        self.__area = a
        self.__perimetro = 2 *(a + b)

    def __obtenerArea(self):
        return self.__area

    def __obtenerPerimetro(self):
        return self.__perimetro

    area = property(fget= __obtenerArea)
    perimetro = property(fget= __obtenerPerimetro)


r = Rectangulo(2,3)
print('A: ', r.area, 'P: ', r.perimetro)