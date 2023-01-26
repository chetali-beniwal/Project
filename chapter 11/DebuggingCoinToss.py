import random
guess=''
while guess not in ('heads', 'tails'):
    guess=input('Guess the coin toss! Enter heads or tails:')
toss=random.randint(0,1)
if toss==1:
    toss='heads'
else:
    toss='tails'
if guess==toss:
    print('you got it')
else:
    print('nope! guess again')
    guess=input()
    if guess==toss:
        print('you got it')
    else:
        print('you are really bad at this game')