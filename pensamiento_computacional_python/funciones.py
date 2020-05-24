import time
print("""============================================================
============================================================
         mi primer programa con funciones UwU
============================================================
============================================================""")
time.sleep(2)
print('''
•primero escogers el numero con el que realizars el calculo

•luego escogeras la opcion con la cual haras el calculo''')
numero = int(input('escoge el numero: '))
time.sleep(2)
print('''ahora escoge la forma con la que realizaras el calculo
- (1) opcion 1
- (2) opcion 2
- (3) opcion 3''')
def opcion1(numero):
    print(numero, 'opcion 1')
    
def opcion2(numero):
    print(numero,'opcion 2')
    
def opcion3(numero):
    print('.')
        
time.sleep(2)
while True:
    opcion = int(input('ingrese el numero que desea usar: '))
    if opcion == 1:
        opcion1(numero)
        time.sleep
        print('adios')
        break
    elif opcion == 2:
        opcion2(numero)
        time.sleep(2)
        print('adios')
        break
    elif opcion == 3:
        opcion3(numero)
        time.sleep(2)
        print('adios')
        break
    else:
        print('esa no es una opcion UnU')
        time.sleep(2)
        break