List1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
List2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
List3 = []

for elements1 in List1:
    for elements2 in List2:
        if elements1 == elements2 and elements1 not in List3:
            List3.append(elements1)
print('Wspólne warttości dwóch danych list: {}' .format(List3))

import random
RandomQuantityForList4 = random.randint(1,10)
RandomQuantityForList5 = random.randint(1,10)
List4 = []
List5 = []
List6 = []

for i in range(RandomQuantityForList4):
    List4.append(random.randint(1,10))
for i in range(RandomQuantityForList5):
    List5.append(random.randint(1,10))
    
print('Pierwsza losowa lista: {}' .format(List4))   
print('Druga losowa lista: {}' .format(List5))

for elements4 in List4:
    for elements5 in List5:
        if elements4 == elements5 and elements4 not in List6:
            List6.append(elements4)
print('Wspólne warttości dwóch losowych list: {}' .format(List6))
