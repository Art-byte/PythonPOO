
class animal:
    def acciones(self):
        return []

class perro(animal):
    def acciones(self):
        return ['ladrar',
                'comer',
                'caminar',
                'respirar']

class ave(animal):
    def acciones(self):
        return['volar',
                'comer',
                'respirar',
                'picotear']


a = ave()
p = perro()

def polimorfismo(animal):
    return animal.acciones()


print(polimorfismo(a))
print(polimorfismo(p))