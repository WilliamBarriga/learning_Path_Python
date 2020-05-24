import random

def busqueda(lista, comienzo, final, objetivo):
    print(f'buscando entre {comienzo} y {final}.')
    if comienzo > final:
        return False
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return True
    elif lista[medio] < objetivo:
        return busqueda(lista, medio + 1, final, objetivo)
    elif lista[medio]:
        return busqueda(lista, comienzo, medio - 1, objetivo)


if __name__ == "__main__":
    tamano_lista = int(input('tamaño de la lista: '))
    objetivo = int(input('que numero quieres encontrar: '))

    lista = sorted([random.randint(0,100) for i in range(tamano_lista)])
    
    encontrado = busqueda(lista, 0, len(lista), objetivo)
    
    print(lista)
    print(encontrado)
    print(f'el elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
