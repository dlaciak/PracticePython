import random

if __name__ == "__main__":

    password = []

    SpecialSingLenght = random.randint(3,6)
    DigitLenght = random.randint(3,6)
    SmallLetters = random.randint(8,13)
    BigLetters = random.randint(8,13)

    for i in range(SpecialSingLenght):
        password.append(random.choice('!@#$%^&*()_-'))
    for i in range(DigitLenght):
        password.append(random.choice('0123456789'))
    for i in range(SmallLetters):
        password.append(random.choice('abcdefghijklmnoprstuwxyzvq'))
    for i in range(BigLetters):
        password.append(random.choice('ABCDEFGHIJKLMNOPRSTUWXYZVQ'))

    random.shuffle(password)
    password = "".join(password)

    print('Wygenerowane dla Ciebie hasło to: {}' .format(password))




