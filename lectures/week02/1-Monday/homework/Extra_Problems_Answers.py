


################### 1. Write a function called power which accepts a base and an exponent.
# The function should return the power of the base to the exponent.


# ----------------------------ANSWERS ------------------------------------
# base = 4
# exponent = 2
# def power(base,exponent):
#     product = base**exponent
#     print(f"{base} to the power of {exponent} is {product}")

# power(2,4)

# -------------------VERONICA'S ANSWER-------------------------------------

# -------example---------------

# def nums(count):
#     if count == 0:
#         return
#     else: 
#         print(count)
#     return nums(count-1)

# nums(12)

# --------Veronica's answer ------------------

# def power(base, exponent):
#     if exponent == 0:
#         return 1
    
#     return base * power(base, exponent-1)

# print(power(4,3))
############### 2. Write a function factorial which accepts a number and returns
# the factorial of that number.  A factorial is the product of an
# interger and all the integers below it; eg. , factorial four( 4!) is
# equal to 24, because 4 * 3 * 2 * 1 equals 24.  factorial zero (0!) is always 1.

# -----------------------------ANSWERS -------------------------------------------
# the_number = 0


# def factorial(a_number):
#     product = 1
#     while a_number > 1: 
#         product = product*a_number
#         a_number -= 1
        
#     print(product)

# factorial(the_number)

############### 3. Write a function called recursiveRange which accepts a number and adds up all
# the numbers from 0 to the number passed to the function

# -------------------------------ANSWERS -------------------------------------------------------
# the_num = 1

# def recursiveRange(a_num):
#     sum = 0
#     for i in range(a_num+1):
#         sum = sum+i
#     print(sum)

# recursiveRange(the_num)

################# 4. Write a recursive function called reverse which accepts
# a string and returns a new string in reverse.

# ---------------------------------ANSWERS -------------------------------------------------

# def reverse():
#     pass

# reverse()
