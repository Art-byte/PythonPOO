
class matematica:

    def __fpotencia(base, exponente):
        return base ** exponente

    def __fraiz(n):
        return pow(n, 0.5)

    def __fesprimo(n):
        n = abs(n)
        if n <= 1:return False
        for i in range(2, round(pow(n, 0.5))+1):
            if(n %i==0):
                return False
        return True

    potencia = staticmethod(__fpotencia)
    raiz = staticmethod(__fraiz)
    primo = staticmethod(__fesprimo)

m = matematica()
print(matematica.potencia(2,3))
print(matematica.raiz(5))
print(matematica.primo(13))



