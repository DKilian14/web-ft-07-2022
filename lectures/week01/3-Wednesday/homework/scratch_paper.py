n = int(input("number of rows: "))

for i in range(n):
    for column in range(n-i-1):
        print(" ",end='')
    for column in range(2*i+1):
        print("*", end='')
    print() 
    