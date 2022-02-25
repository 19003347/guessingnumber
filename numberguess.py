import random
number=random.randint(1,20)


choice=1
balance=2
while True:
    print('Guess the random number: ', end='')
    n=int(input())
    if choice==3:
        print('\n------Game Over-----\n')
        print('You Lose')
        break
    if(n==number):
        print('YOU Win')
        break
    elif(n!=number):
        print(f'Only {balance} chance.......')
        choice+=1
        balance-=1



