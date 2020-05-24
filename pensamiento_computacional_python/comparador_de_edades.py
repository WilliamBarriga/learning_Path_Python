print('-------------------------------------------------------------')
print('                   comparador de edades')
nombre1 = input('como es tu nombre: ')
print('hola', nombre1)
nombre2 = input('como es el nombre de la otra persona: ')
print('ahora vamos a comparar la edad tuya con la de', nombre2)
print('primero')
numero1 = int(input('escribe tu edad (solo el numero) : ' ))
numero2 = int(input(f'ahora escribe la edad de {nombre2}:'))
if numero1 > numero2:
    print('genial eres mayor que', nombre2)
elif numero1 == numero2:
    print(nombre2, 'tiene la misma edad que tu |UwU|')
else:
    print('oh!...  parece que', nombre2, 'es mayor que tu')