def even_or_odd(number):
    if (number % 2) == 0:
        return 'Even'
    else:
        return 'Odd'


if __name__ == "__main__":
    number = int(input('select a number: '))
    print(even_or_odd(number))
    