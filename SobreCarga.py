
class mi_numero:

    __valor = 0

    def __init__(self, v):
        self.__valor = v

    def __add__(self, other):
        return(self.__valor + other.__valor)/2

    def __sub__(self, other):
        return(self.__valor - other.__valor)/2

    def __mul__(self, other):
        return(self.__valor * other.__valor)/2

    def __gt__(self, other):
        return self.__valor > other.__valor

    def __neg__(self):
        return self.__valor < 0

    def __bool__(self):
        return self.__valor > 0

    def __eq__(self, other):
        return abs(self.__valor - other.__valor) <= 1

    
n = mi_numero(5)
m = mi_numero(6)

print(n==m)
print(n<m)
print('suma: ', n + m)
print('resta: ', n -m)
print('mult: ', n * m)
print(not mi_numero(-6))