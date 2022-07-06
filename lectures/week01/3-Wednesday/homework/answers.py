

width= int(input("width? "))
height = int(input('height? '))

for i in range(height) :
    if i == 0 or i == height-1 :
        print('*'*width)
    else:
        print('*'+(" "*(width-2)+'*'))