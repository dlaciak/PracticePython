import datetime
now = datetime.datetime.now()

Name = input('Jak masz na imię?\n')
Age = int(input('Ile masz lat?\n'))
Year = now.year

String = '{}!, skończysz 100 lat w roku {}' .format(Name, Year-Age+100)
print(String)

Number = int(input('Wprowadź liczbę naturalną\n'))
print(String * Number)

print((String + '\n') * Number )
