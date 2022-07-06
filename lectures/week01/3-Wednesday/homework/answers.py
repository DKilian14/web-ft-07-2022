
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