'program z cw5 tylko z użyciem List Overlap Comprehensions

import random

List1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
List2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
NewList = []

[NewList.append(element) for element in List1 for element2 in List2 if element == element2 and element not in NewList]
print(NewList)

RandomQuantityForList3 = random.randint(1,10)
RandomQuantityForList4 = random.randint(1,10)
List3 = []
List4 = []
NewList2 = []

[List3.append(random.randint(1,10)) for i in range(RandomQuantityForList3)]
[List4.append(random.randint(1,10)) for i in range(RandomQuantityForList4)]

print('Pierwsza losowa lista: {}' .format(List3))   
print('Druga losowa lista: {}' .format(List4))

[NewList2.append(element) for element in List3 for element2 in List4 if element == element2 and element not in NewList2]
print('Wspólne warttości dwóch losowych list: {}' .format(NewList2))

