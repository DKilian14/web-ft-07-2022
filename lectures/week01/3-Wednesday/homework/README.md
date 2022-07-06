# Homework

## Python 101

#### 1. Tip Calculator

Your task is to write a program that calculates how much of a tip to leave at a restaurant.

Prompt the user for two things:

- The total bill amount
- The level of service, which can be one of the following: good, fair, or bad

Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

- good -> 20%
- fair -> 15%
- bad -> 10%

Example session:

```
$ python3 tip_calc.py
Total bill amount? 100
Level of service? good
Tip amount: $20.00
Total amount: $120.00
```

```
$ python3 tip_calc.py
Total bill amount? 48
Level of service? bad
Tip amount: $4.80
Total amount: $52.80
```

Hints:

- Remember that you need to convert the input from the user input to floats instead of ints. Use the `float` function instead of the `int` function.
- To format a float number as a dollar value, use Python's formatting syntax: `"%.2f" % amount`



def calculate():
    total_bill = float(input("what is the bill total?: "))
    service = input(
        """
    Was the service: 
    good 
    fair 
    bad   
    """
    )
    
    if (service == 'good') :
        tip = "%.2f" % (total_bill*.20) 
    elif (service =='fair') :
        tip = "%.2f" % (total_bill*.15) 
    elif (service == 'bad'):
        tip = "%.2f" % (total_bill*.10) 
    else: 
        return print("next time, enter the service as either 'good','fair', of 'bad'.")


    print(f'tip amount: {tip}')
    print(f'total amount: {total_bill}')
    

tip_total = calculate()

#### 2. Tip Calculator 2

Allow the ability to divide the check into a equal parts amount a number of people. The user will enter the number of people to be divided amongst. Example session:

```
$ python3 tip_calc2.py
Total bill amount? 100
Level of service? good
Split how many ways? 5
Tip amount: $20.00
Total amount: $120.00
Amount per person: $24.00
```


def calculate():
    guests = int(input("Split how many ways?"))
    total_bill = float(input("what is the bill total?: "))
    service = input(
        """

    Was the service: 
    good 
    fair 
    bad   
    """
    )
    total_per_guest = total_bill/guests

    

    if (service == 'good') :
        tip = "%.2f" % (total_bill*.20) 
    elif (service =='fair') :
        tip = "%.2f" % (total_bill*.15) 
    elif (service == 'bad'):
        tip = "%.2f" % (total_bill*.10) 
    else: 
        return print("next time, enter the service as either 'good','fair', of 'bad'.")


    print(f'tip amount: {tip}')
    print(f'total amount: {total_bill}')
    print(f'Amount per person: {total_per_guest}')


calculated_total = calculate()

#### 3. How many coins?

Write a program that will prompt you for how many coins you want. Initially you have no coins. It will ask you if you want a coin? If you type "yes", it will give you one coin, and print out the current tally. If you type no, it will stop the program. Example run:

```
$ python3 coins.py
You have 0 coins.
Do you want another? yes
You have 1 coins.
Do you want another? yes
You have 2 coins.
Do you want another? no
Bye
```

want_coins = 'yes'
num_coins = 0

while want_coins == 'yes':
    print(f'you have {num_coins} coin(s)')
    want_coins = input("would you like a coin [yes/no]? ")
    if want_coins == 'yes':
        num_coins+=1
    else:
        print('bye')

#### 4. Print a Box

Given a height and width, input by the user, print a box consisting of * characters as its border. Example session:

```
$ python3 box.py
Width? 6
Height? 4
******
*    *
*    *
******
```

width= int(input("width? "))
height = int(input('height? '))

for i in range(height) :
    if i == 0 or i == height-1 :
        print('*'*width)
    else:
        print('*'+(" "*(width-2)+'*'))

#### 5. Print a Triangle

Print a triangle consisting of * characters like this:

```
   *
  ***
 *****
*******
```

print(
    """
    *
   ***
  *****
 *******
    """
)

#### 6. Multiplication Table

Print the multiplication table for numbers from 1 up to 10. Example output:

```
$ python3 multiplication_table.py
1 X 1 = 1
1 X 2 = 2
1 X 3 = 3
1 X 4 = 4
...
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
...
10 X 8 = 80
10 X 9 = 90
10 X 10 = 100
```

## Submit Homework
- Create an issue
- Title issue: Python101_[YourName] i.e. Python101_VeronicaLino