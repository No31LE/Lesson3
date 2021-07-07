import random
i = 0
y = -1

x = random.randint(1,20)
while i < 5 and x != y:
    
    y = int(input('''number?
'''))
    if x == y:
        print('you guessed it!')
        print('it took you',i+1,'tries')
    elif i == 4 :
        print('GAME OVER')
        print('the number was',x)
    elif y > x:
        print('too large')
        print('guess again')
    else:
        print('too small')
        print('guess again')
    i = i+1