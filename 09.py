import random
import datetime

Time = datetime.datetime.now()
print('Aktualny czas: {}' .format(Time))
Counter = 1
print('Zostanie wylosowana liczba z zakresu 1-9. Odgadnij ją.')

while 1:
    if Counter == 1:
        RandomNumber = random.randint(1,9)
    GuessedNumber = int(input('Wprowadź liczbę\n'))
    if GuessedNumber < RandomNumber:
        print('Za mała')
        Counter+=1
    elif GuessedNumber > RandomNumber:
        print('Za duża')
        Counter+=1
    else:
        print('Brawo')
        print('Ilość prób: {}' .format(Counter))
        Continue = input('Aby wyjść wprowadź "exit", aby zagrać jeszcze raz cokolwiek innego.\n')
        if Continue == 'exit':
            break
        else:
            Counter = 1
