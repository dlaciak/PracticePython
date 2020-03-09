def InputNumber(Text):
    return int(input(Text))

def Fibonacci(Number):
    List = [1, 1]
    for i in range(Number-2):
        List.append(List[i] + List[i+1])
    return List


Number = InputNumber('Wprowadź liczbę naturalną: ')
List = Fibonacci(Number)
print(List)
