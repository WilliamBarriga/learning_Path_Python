import random

def ordeamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - i -1):
            if lista[j] > lista[j + 1]:
                print(lista)
                lista[j], lista[j +1] = lista[j +1], lista[j]
    return lista
if __name__ == "__main__":
    tamano_lista = int(input('tamano de la lista: '))

    lista = [random.randint(0, 100)for i in range(tamano_lista)]
    print(lista)

    lista_ordenada = ordeamiento_burbuja(lista)
    print('lista finales')
    print(lista_ordenada)