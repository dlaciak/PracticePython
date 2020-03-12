Word = input('Wprowadź słowo\n')
CzyPalindrom = True
i=1

for letter in Word:
    if letter == Word[len(Word)-i]:
        i+=1
    else:
        CzyPalindrom = False
        break

if CzyPalindrom:
    print(Word + ' jest palindromem')
else:
    print(Word + ' nie jest palindromem')

'to samo inaczej'

if Word == Word[::-1]:
    print(Word + ' jest palindromem')
else:
    print(Word + ' nie jest palindromem')
