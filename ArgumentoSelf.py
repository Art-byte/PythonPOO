class auto:
    __millas = 0
    __marca = ''
    def __init__(self, marca, millas):
        self.__millas = millas
        self.__marca = marca

    def obtenerMillas(self):
        return self.__millas

    def obtenerMarca(self):
        return self.__marca


def f():
    print('Un auto')


auto.imprime = f
auto.imprime()

bmw.imprime()

#Bmw debera devolver un error ya que no existe en el contexto actual de clase 
