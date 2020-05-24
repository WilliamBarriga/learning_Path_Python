#0-1 knaksack

def morral(tamano_morral, pesos, valores, n):
    
    if n == 0 or tamano_morral == 0:
        return 0
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)
    
    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1),
                morral(tamano_morral, pesos, valores, n - 1))

if __name__ == "__main__":
    valores = [60, 100,120]
    pesos = [10, 20, 30]
    tamano_morral = int(input('de que tamano va a ser tu morral: '))
    n = len(valores)

    resultado = morral(tamano_morral, pesos, valores, n)
    print(f'lo maximo que puedes escoger con un morral de {tamano_morral} es {resultado}')