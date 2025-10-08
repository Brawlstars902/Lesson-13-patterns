r=int(input('Please enter the number of rows you would like to make a diamond.         '))
if r%2==0:
    h=int(r/2)
else:
    h=int(r/2)+1
s=h-1
for i in range(1,h+1):
    for j in range(1, s+1):
        print(end=' ')
    s=s-1
    n=1
    for j in range(2*i-1):
        print(end=str(n))
        n=n+1
    print()
s=1
for i in range(1,h):
    for j in range(1,s+1):
        print(end=' ')
    s=s+1
    n=1
    for j in range(1,2*(h-i)):
        print(end=str(n))
        n=n+1
    print()