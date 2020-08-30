class Largometraje:
    duracion = 0
    titulo = ""

    def obtenerDuracion(self):
        return self.duracion
    
    def indicarDuracion(self, duracion):
        self.duracion = duracion

    def obtenerTitulo(self):
        return self.titulo

    def indicarTitulo(self, titulo):
        self.titulo = titulo


class Drama(Largometraje):
    cargaDramatica = 0

    def obtenerCarga(self):
        return self.cargaDramatica

    def indicarCarga(self, cargaDramatica):
        self.cargaDramatica = cargaDramatica


class Oeste (Largometraje):

    pistoleros = 0

    def obtenerPistoleros(self):
        return self.pistoleros

    def indicarPistoleros(self, pistoleros):
        self.pistoleros = pistoleros


class Imperdonable(Drama, Oeste):
    pass

i = Imperdonable()
i.indicarCarga(2)
i.indicarDuracion(120)
i.indicarTitulo("Imperdonable")
i.indicarPistoleros(2)

print('Carga', i.obtenerCarga())
print('Duracion', i.obtenerDuracion())
print('Titulo', i.obtenerTitulo())
print('Pistoleros', i.obtenerPistoleros())


