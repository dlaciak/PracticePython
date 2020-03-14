def CasualSearch(List,Number):
    if Number in List:
        return True
    else:
        return False

def BinarySearch(List,Number):
     
    while 1:
        if List[(len(List)-1)//2] == Number:
            return True
        elif List[(len(List)-1)//2] > Number:
            List=List[0:(len(List)-1)//2:]
            if len(List) == 1:
                if List[0] == Number:
                    return True
                else:
                    return False
        else:
            List=List[(len(List))//2::]
            if len(List) == 1:
                if List[0] == Number:
                    return True
                else:
                    return False


if __name__ == "__main__":

    List = [1,3,5,7,8,10,12,15,17,19,21,25,26,30,35,54,83,84]
    Number = int(input())

    IsOnList = CasualSearch(List,Number)
    print('Rezultat wyszukiwania liczby {} na liście to: {}' .format(Number,IsOnList))
    IsOnList = BinarySearch(List,Number)
    print('Rezultat wyszukiwania liczby {} na liście za pomocą binary search to: {}' .format(Number,IsOnList))



   



    
    

        
    
