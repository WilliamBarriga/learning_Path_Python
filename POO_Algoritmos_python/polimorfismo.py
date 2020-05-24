class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    def avanzar(self):
        print(f'me llamo {self.nombre} y estoy caminando')

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)
    def avanzar(self):
        print(f'soy {self.nombre} y estoy en mi cicla')


def main():
    nombre = input('como te llamas: ')
    persona = Persona(nombre)
    ciclista = Ciclista(nombre)
    persona.avanzar()
    ciclista.avanzar()


if __name__ == '__main__':
    main()