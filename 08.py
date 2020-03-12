print('Rock, Paper, Scissors Game\nType R - rock, P - paper - S - Scissors or any other button to exit')

while 1:
    Player1Choice = input('Player 1 turn\n')
    if Player1Choice != 'R' and Player1Choice != 'S' and Player1Choice != 'P':
        break
    Player2Choice = input('Player 2 turn\n')
    if Player2Choice != 'R' and Player2Choice != 'S' and Player2Choice != 'P':
        break
    if Player1Choice == Player2Choice:
        print('Draw')
    elif Player1Choice == 'R' and Player2Choice == 'S' or Player1Choice == 'P' and Player2Choice == 'R' or Player1Choice == 'S' and Player2Choice == 'P':
        print('Player 1 won')
    else:
        print('Player 2 won')
    Continue = (input('Do you want to continue? Type "yes"\n'))
    if Continue != 'yes':
        break
