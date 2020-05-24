n = int(input('ingresa n: '))
def a(n): #la secuencia de fibonacci UwU
    if n == 0 or n == 1:
        print (n)
        return 1
    return a(n - 1) + a(n - 2)
print (a(n))