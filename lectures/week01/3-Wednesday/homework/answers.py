
num = int(input('Provide a number you would like the factors to: '))

factors = []

for every_number in range(1,num+1):
    if num % every_number == 0:
        factors.append(every_number)

print(f'Factors of {num} is {factors}')