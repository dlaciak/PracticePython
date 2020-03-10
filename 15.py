def ReverseWordOrder(txt):
    txt2 = " ".join(txt.split()[::-1])
    return txt2

txt1 = input('Wprowadź długie zdanie\n')
txt2 = ReverseWordOrder(txt1)
print(txt2)


