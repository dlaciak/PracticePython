import random

def RandomFourDigitNumber():
    Number = random.sample(range(10),4)
    return list(Number)

def InputFourDigitNumber():
    IsCorrect = True
    while IsCorrect:
        UserNumber = (input('Wprowadź 4 cyfry\n'))
        if UserNumber[0] != UserNumber[1] and UserNumber[0] != UserNumber[2] and UserNumber[0] != UserNumber[3] and UserNumber[1] != UserNumber[2] and UserNumber[1] != UserNumber[3] and UserNumber[2] != UserNumber[3]:
            IsCorrect = False
        else:
            print('Wprowadzono nieprawidłową liczbę')
    UserNumber = list(UserNumber)
    return UserNumber

if __name__ == "__main__":

    print('Krowa - cyfra na prawidłowej pozycji, Byk - poprawna cyfra na złej pozycji')
    Cow = 0
    Bull = 0
    RandomNumber = (RandomFourDigitNumber())
    Counter = 0

    while Cow!=4:
        if Counter > 0:
            print('Spróbuj ponownie\n')
        Cow = 0
        Bull = 0
        UserNumberList =[]
        UserNumber = InputFourDigitNumber()
        for i in range(4):
            UserNumberList.append(int(UserNumber[i]))

        for i in range(4):
            if RandomNumber[i] == UserNumberList[i]:
                Cow += 1
            for j in range(4):
                if i != j:
                    if RandomNumber[i] == UserNumberList[j]:
                        Bull += 1
        print('Liczba krów to {}' .format(Cow))
        print('Liczba byków to {}' .format(Bull))
        Counter += 1

    print('Gratulacje wygrałeś. Ilość prób: {}' .format(Counter))
  
    
      
    


 
    

    
   

