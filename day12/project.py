import random

print('welcome to the Number Guessing Game')
print('Number is between 1 and 100')

level=input("Choose a difficulty. Type 'easy' or 'hard- ")
number=random.randint(0,100)

if level == 'easy':
    attemps= 10
else :
    attemps=5


guess=int(input('Make a guess- '))

while guess!=number and attemps!=1 :
    
    if guess>number :
        print('too high')
    else:
        print('too low')
    guess=int(input('Make a guess- '))
    attemps=attemps-1
    

if guess==number:
    print('you won man')
else: 
    print('you loss man')