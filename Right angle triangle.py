n=int(input('Please enter the amount of rows to create a right angled triangle made of stars(*)\n'))
for i in range(n):
    for j in range(i+1):
        print('*',end=" ")
    print ()