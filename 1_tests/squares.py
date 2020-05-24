import math
def square(n):
    if n < 0:
        return False
    sqrt = math.sqrt(n)

    return sqrt.is_integer()      



if __name__ == "__main__":
    n = int(input('select a number: '))
    print(square(n))