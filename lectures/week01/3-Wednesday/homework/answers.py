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