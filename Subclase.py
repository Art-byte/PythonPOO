class miCadena(str):

    def es_palindromo(self):
        if len(self) is 1:
            return True

        j = len(self) - 1
        for i in range(len(self)):
            if self[i] != self[j]:
                return False

            j-=1
            if i == j: break
        return True

    def es_anagrama(self, x):
        for i in range(len(self)):
            if x.count(self[i]) != \
                self.count(self[i]):
                return False

        for i in range(len(x)):
            if x.count(x[i]) !=\
                self.count(x[i]):
                return False
        
        return True


s = miCadena('anitalavalatina')
print(s.es_palindromo())
print(s.es_anagrama('sasatvv'))