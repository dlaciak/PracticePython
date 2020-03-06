List = [1, 12, 28, 3, 5, 55, 21, 8, 2, 13, 7]
ListOfVariableLessThan5 = []
ListOfVariableLessThanNumber = []
print('Elementy listy mniejsze od 5: ',end='')

for i in List:
    if i < 5:
        print(i,end=' ')
        ListOfVariableLessThan5.append(i)
        
print('\nLista utworzona z tych elementów: {}' .format(ListOfVariableLessThan5))

Number = int(input('Wprowadź liczbę.\n'))
for i in List:
    if i < Number:
        ListOfVariableLessThanNumber.append(i)
print('\nLista liczb mniejszych od {}: {}' .format(Number,ListOfVariableLessThanNumber))

