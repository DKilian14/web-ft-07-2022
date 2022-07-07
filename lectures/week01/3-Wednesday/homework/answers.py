#Question 1. 

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
        tip = total_bill* .2
    elif (service =='fair') :
        tip = total_bill*.15
    elif (service == 'bad'):
        tip = total_bill*.10
    else: 
        return print("next time, enter the service as either 'good','fair', of 'bad'.")

    total_bill = total_bill + tip

    print(f'tip amount: {"%.2f" % tip}')
    print(f'total amount: {"%.2f" % total_bill}')
    

tip_total = calculate()

#Question 2. 

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
    
    
    
    if (service == 'good') :
        tip = total_bill* .2
    elif (service =='fair') :
        tip = total_bill*.15
    elif (service == 'bad'):
        tip = total_bill*.10
    else: 
        return print("next time, enter the service as either 'good','fair', of 'bad'.")

    total_bill = total_bill + tip
    total_per_guest = total_bill/guests

    print(f'tip amount: {"%.2f" % tip}')
    print(f'total amount: {"%.2f" % total_bill}')
    print(f'Amount per person: {total_per_guest}')

tip_total = calculate()

#Question 3. 

want_coins = 'yes'
num_coins = 0

while want_coins == 'yes':
    print(f'you have {num_coins} coin(s)')
    want_coins = input("would you like a coin [yes/no]? ")
    if want_coins == 'yes':
        num_coins+=1
    else:
        print('bye')
        
        
#Question 4. 

width= int(input("width? "))
height = int(input('height? '))

for i in range(height) :
    if i == 0 or i == height-1 :
        print('*'*width)
    else:
        print('*'+(" "*(width-2)+'*'))
        
        
#Question 5. 

print(
    """
    *
   ***
  *****
 *******
    """
)


# Question 6. 

limit = 10

for i in range(1, limit+1):
    for j in range(1, limit+1):
        print(f'{i}*{j}={i*j}')


#Extra Challenge 1. 

triangles_to_try = 100

for  each_triangle in range(1,triangles_to_try+1):
    tri_num = (each_triangle * (each_triangle+1))/2
    print(f'triangle {each_triangle} has a triangle number of {tri_num}')


#Extra Challenge 2. 

num = int(input('Provide a number you would like the factors to: '))

factors = []

for every_number in range(1,num+1):
    if num % every_number == 0:
        factors.append(every_number)

print(f'Factors of {num} is {factors}')