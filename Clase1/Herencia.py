class edificacion:

    def __init__(self, altura, duenio, precio, ubicacion):
        self.altura = altura
        self.duenio = duenio
        self.precio = precio
        self.ubicacion = ubicacion

#Definimos Gets y Sets

    def obtenerAltura(self):
        return self.altura

    def indicarAltura(self,altura):
        self.altura = altura

    def obtenerDuenio(self):
        return self.duenio
        
    def indicarDuenio(self,duenio):
        self.duenio = duenio

    def obtenerPrecio(self):
        return self.precio
        
    def indicarPrecio(self, precio):
        self.precio = precio

    def obtenerUbicacion(self):
        return self.ubicacion
        
    def indicarUbicacion(self, ubicacion):
        self.ubicacion = ubicacion



class casa(edificacion):

    habitantes = 0
    def __init__(self, altura, duenio, precio, ubicacion, habitantes):
        super().indicarAltura(altura)
        super().indicarDuenio(duenio)
        super().indicarPrecio(precio)
        super().indicarUbicacion(ubicacion)
        self.habitantes = habitantes

    def obtenerHabitantes(self):
        return self.habitantes
    


class Comercializadora(edificacion):

    areas_comerciales = []

    def __init__(self, altura, duenio, precio, ubicacion, areas_comercio):
        super().indicarAltura(altura)
        super().indicarDuenio(duenio)
        super().indicarPrecio(precio)
        super().indicarUbicacion(ubicacion)
        self.areas_comercio = areas_comercio

    def obtenerAreasComercio(self):
        return self.areas_comercio


    

