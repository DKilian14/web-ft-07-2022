
#1. Create a program that will print from 1-10 using a while loop.

# num=1
# while num <= 10:
#     print(num)
#     num += 1

#2. Create a program that will print from 10-1 using a while loop.

# num=10
# while num > 0:
#     print(num)
#     num -= 1

#3. Create a program that prompts the user to enter a word.  The program doesn't stop asking the user to enter a word until the user enters the word "stop"


# word = ''
# while word != 'stop':
#     word = input('enter a word. Type "stop" to stop entering words.')

#4a. Create a program that has a variable named username and another variabled named password with values of your choice.
    #4b. Prompt the user for a username and then a password.
        #4c. If the both match continue on with the program and give a welcome message.
            #4d. If not it prompts the user for the username and password until they get it correct.
                #4e. (bonus) have a limited amount of attempts and if they reach the limit it tells the user and exits the program.

username = 'DkillaK'
password = 'password123!'

login_attempt_username = "".lower()
login_attempt_password = "".lower()
attempts = 0

while (login_attempt_username != username or login_attempt_password != password) and attempts < 5: 
    login_attempt_username = input('enter a username')
    login_attempt_password = input('enter a password')
    attempts += 1
    if login_attempt_username == username and login_attempt_password == password: 
        print('welcome!')
    elif attempts == 5:
        print('too many attempts. Restart program and try again.')


#4e. (bonus) have a limited amount of attempts and if they reach the limit it tells the user and exits the program.

# saved_password = 'pass123'
# saved_username = "Dan"

# attempted_password = ''
# attempted_username = ''

# attempts = 0

# while (attempted_password != saved_password or attempted_username != saved_username) and attempts < 5:
#     attempted_username = input('Enter username: ')
#     attempted_password = input('Enter password: ')
#     attempts += 1
#     if attempted_password == saved_password or attempted_username == saved_username:
#         print('Welcome!')
    

