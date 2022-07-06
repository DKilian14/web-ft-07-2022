## Extra Challenge

#### 1. Triangle Numbers

Print the first 100 triangle numbers. What is a triangle number? Read 
[this article to find out what triangle numbers are](https://www.mathsisfun.com/algebra/triangular-numbers.html).

triangles_to_try = 100

for  each_triangle in range(1,triangles_to_try+1):
    tri_num = (each_triangle * (each_triangle+1))/2
    print(f'triangle {each_triangle} has a triangle number of {tri_num}')


#### 2. Factor a Number

Given a number, print its factors. What are factors? Read through [this article on finding the factors of a number](https://www.khanacademy.org/math/pre-algebra/factors-multiples/divisibility-and-factors/v/finding-factors-of-a-number
).

num = int(input('Provide a number you would like the factors to: '))

factors = []

for every_number in range(1,num+1):
    if num % every_number == 0:
        factors.append(every_number)

print(f'Factors of {num} is {factors}')