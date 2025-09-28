x=int(input('Enter a number: '))
n=1
for i in range(1,x+1):
    for b in range(1,i+1):
        print(n, end=' ')
        n=n+1
    print( )