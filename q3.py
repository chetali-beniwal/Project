import sys
def collatz(n):
    if n%2==0:
        print(n//2)
        return n//2
    else:
        print(3*n+1)
        return 3*n+1
try:
    print("Enter number:")
    n=int(input())
    x=collatz(n)
    while True:
        if x==1:
            sys.exit()
        else:
            x=collatz(x)
except ValueError:
    print('enter an integer')