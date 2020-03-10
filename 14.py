def RemoveDuplicatesLoop(List):
    NewList = []
    [NewList.append(element) for element in List if element not in NewList]
    return NewList

def RemoveDuplicatesSet(List):
    return list(set(List))


List1 = [1, 1, 2, 3, 5, 8, 13, 13, 21, 34, 34, 34, 34, 55, 89]
NewList1 = RemoveDuplicatesLoop(List1)
print(NewList1)
NewList2 = RemoveDuplicatesSet(List1)
print(NewList2)

#ex 5 

List1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
List2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
NewList=[]
[NewList.append(element) for element in List1 for element2 in List2 if element == element2 and element not in NewList]
print(NewList)

#ex5 set

def WspolneBezPowtorzen(List1,List2):
    NewList=[]
    [NewList.append(element) for element in List1 for element2 in List2 if element == element2]
    return list(set(NewList))

NewList2 = []
NewList2 = WspolneBezPowtorzen(List1,List2)
print(NewList2)
