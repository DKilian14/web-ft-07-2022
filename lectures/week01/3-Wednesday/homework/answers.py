


want_coins = 'yes'
num_coins = 0

while want_coins == 'yes':
    print(f'you have {num_coins} coin(s)')
    want_coins = input("would you like a coin [yes/no]? ")
    if want_coins == 'yes':
        num_coins+=1
    else:
        print('bye')