'to samo co ćw 4. tylko na sterydach'

def IsPrime(Number):
    ListOfNumbers = range(2,Number)
    Divisors = []
    [Divisors.append(elements) for elements in ListOfNumbers if Number % elements == 0]
    if len(Divisors) == 0:
        return True
    else:
        return False






Liczba = int(input('Wprowadź liczbę naturalną. '))
if Liczba != 1 and IsPrime(Liczba) == True:
    print('Podana liczba to liczba pierwsza')
else:
    print('Podana liczba to nie liczba pierwsza')

    

