class ciudad:
    __pais = ''
    __nombre = ''
    __habitantes = 0


    def __init__(self, p, n, h):
        self.__pais = p
        self.__nombre = n
        self.__habitantes = h

    def numeroHabitantes(self):
        return self.__habitantes

    numero_habitantes = property\
        (fget = numeroHabitantes)

class habana(ciudad):

    def __init__(self, p, n):
        super().__init__(p,n,20000000)


h = habana("Cuba", "Habana")

print(h.numero_habitantes)
print(isinstance(h, ciudad))
print(isinstance(h, habana))



