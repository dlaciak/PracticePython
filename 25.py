print('Pomyśl liczbę od 0 do 100, a ja spróbuję ją odgadnąć.')

Start = 0
End = 100
Counter = 0
answer = 'XD psie'
Oszust = False
ComputerGuess = []

while 1:
    
    C = (Start + End)//2
    Counter+=1

    if C not in ComputerGuess:
        ComputerGuess.append(C)
    else:
        Oszust = True
        break
     
    print('Czy Twoja liczba to {}? Wprowadź 0 - Tak, 1 - moja liczba jest wyższa, 2 - moja liczba jest niższa ' .format(C))

    while answer != '0' and answer != '1' and answer != '2':
        answer = input()

    if answer == '0':
        break
    elif answer == '1':
        Start = C+1
    elif answer == '2':
        End = C-1
        
    answer = 'XD psie'
       
if not Oszust:
    print('Zgadłem w {} próbach, EZ' .format(Counter))
else:
    print('Jesteś jebanym kłamliwym psem')
