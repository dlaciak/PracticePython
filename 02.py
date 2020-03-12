import datetime

Time = datetime.datetime.now()

print('Dzisiaj mamy {}.{}.{}r.' .format(Time.day,Time.month,Time.year))
Number = int(input('Wprowadź liczbę\n'))

if Number % 4 == 0:
    print('Liczba jest podzielna przez 4.')
elif Number % 2 == 0:
    print('Liczba jest parzysta.')
else:
    print('Liczba jest nieparzysta.')

Number1 = int(input('Wprowadź pierwszą liczbę\n'))
Number2 = int(input('Wprowadź drugą liczbę różną od 0\n'))
if Number1 % Number2 == 0:
    print('{} jest dzielnikiem {}' .format(Number2,Number1))
else:
     print('{} nie jest dzielnikiem {}' .format(Number2,Number1))
