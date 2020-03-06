import datetime
Time = datetime.datetime.now()
print('Aktualny czas: {}' .format(Time))

Number = int(input('Wprowadź liczbe, zostaną wyświetlone jej dzielniki.\n'))
ListOfNumbers = range(1,Number+1)
Divisors = []

for elements in ListOfNumbers:
    if Number % elements == 0:
        Divisors.append(elements)
print('Lista dzielników: {}' .format(Divisors))
