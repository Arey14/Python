
class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('{Anda caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Anda moviendome en mi bicicleta')

def main():
    persona = Persona('Augusto')
    persona.avanza()

    ciclista = Ciclista('Leo')
    ciclista.avanza()
      
if __name__ == '__main__':
    main()