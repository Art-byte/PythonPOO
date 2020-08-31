class movil:

    marca = ''
    pin = 0

    def __init__(self, m, p):
        self.marca = m 
        self.pin = p
    
    def llamada(cls):
        print("llamando... ") 

    llamar = classmethod(llamada)

iphone = movil('iphone 5', 5432)

movil.llamar()
iphone.llamar()