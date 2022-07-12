

def print_upto_n(n):
    if n > 0: 
        print_upto_n(n-1)
        print(n)
        

print_upto_n(10)




