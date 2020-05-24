import time
print('hello')
time.sleep(2)
class lavadora:
    def __init__(self):
        pass
    def lavar(self, temperatura=input('a que temperatura: '), cantidad_de_agua =input('cantidad de agua: ')):
        self._llenar_tanque(temperatura,cantidad_de_agua)
        self._anadir_jabon()
        self._lavar()
        self._secar()
        self._terminado()
    def _llenar_tanque(self, temperatura, cantidad_de_agua):
        print(f'llenando tanque con agua{cantidad_de_agua}, y temperatura {temperatura}')
        time.sleep(1)
    def _anadir_jabon(self):
        print('añadiendo jabon')
        time.sleep(1)
    def _lavar(self):
        print('lavando')
        time.sleep(1)
    def _secar(self):
        print('secando')
        time.sleep
    def _terminado(self):
        print('terminado')

if __name__ == '__main__':
    print('iniciando')
    time.sleep(3)
    Lavadora = lavadora()
    Lavadora.lavar()