
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

    print(total_bill)

    if (service == 'good') :
        return print("%.2f" % (total_bill*.20)) 
    elif (service =='fair') :
        return print("%.2f" % (total_bill*.15))
    elif (service == 'bad'):
        return print("%.2f" % (total_bill*.10))
    else: 
        return print("next time, enter the service as either 'good','fair', of 'bad'.")




tipTotal = calculate()