
import random

def busqueda(lista, objetivo):
    match = False
    for elemento in lista:
        print(elemento)
        if elemento == objetivo:
            match = True
            break
    return match

if __name__ == "__main__":
    tamano_lista = int(input('tamaño de la lista: '))
    objetivo = int(input('que numero quieres encontrar: '))

    lista = [random.randint(0,100) for i in range(tamano_lista)]
    encontrado = busqueda(lista, objetivo)
    
    print(lista)
    print(encontrado)
    print(f'el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
