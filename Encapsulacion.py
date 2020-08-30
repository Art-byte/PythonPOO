class piano:

    __cuerdas = 224
    __teclado = 88
    __fabricante = ''
    __maderas = []

    def __init__(self, fabricante):
        self.__fabricante = fabricante

    def obtenerFabricante(self):
        return self.__fabricante

    def obtenerTeclado(self):
        return self.__teclado

    def obtenerCuerdas(self):
        return self.__cuerdas



class pianista:
    __nombre = ''
    __piano = None

    def __init__(self,nombre):
        self.__nombre = nombre

    def obtenerNombre(self):
        return self.__nombre 

    def indicarNombre(self, nombre):
        self.__nombre = nombre

    def obtenerPiano(self):
        return self.__piano

    def indicarPiano(self,piano):
        self.__piano = piano



beethoven = pianista('beethoven')
beethoven.piano = piano('Steinway y sons')

print(beethoven.piano.obtenerCuerdas())
print(beethoven.piano.obtenerFabricante())
print(beethoven.piano.obtenerTeclado())


