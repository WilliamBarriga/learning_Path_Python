import time
seguir = 'y'
while seguir == 'y':
    numero1 = int(input('escoge un numero: '))
    numero2 = int(input('escoge un numero: '))
    time.sleep(1)
    print(numero1 + numero2)
    seguir = input('y o n:')
time.sleep(1) 
print('finalizado')
