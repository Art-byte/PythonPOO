
""" 
Comenzamos teniendo en cuenta un ejemplo sencillo donde podemos
añadir a un objeto cualquiera una instancia de la clase zapato
y este a su vez, le agregamos  una propiedad

"""
class zapato:
    pass


adidas = zapato()
adidas.costo = 23

#También es posible agregar de manera dinámica metodos a la clase e irlo vinculando
def x():
    return "rojo"
adidas.color = x()


print(adidas.costo)
print('El zapato es de color: ', adidas.color)