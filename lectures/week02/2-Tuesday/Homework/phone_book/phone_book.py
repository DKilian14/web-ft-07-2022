import pickle # Imports a module that allows you to export your data to another file. 
import time

try:
    with open('phonebook.pickle', 'rb') as filehandler:
        phonebook = pickle.load(filehandler)
except:
    phonebook = {'charles': 123}

def print_menu():
    print("""
      
      Electronic Phone Book
==================================
      """)
    count = 1
    for every_menu_item in menu:
        print(f'{count}: {every_menu_item}')
        count +=1
    print("What do you want to do (1-5)?  ")
    
def lookup_number():
    print("looking up number....")
    name = input('What is the name? >>')
    print(phonebook.get(name)) #will print the phone number
    
def set_entry():

    print('setting name....')
    name = input('what is the name?  ')
    number = input('what is the number?  ')
    phonebook[name] = number
    print("added!")

def delete():
    try:
        name = input('what entry would you like to delete?')
        del phonebook[name]
    except:
        print('that is not an existing entry')
    
def list_all():
    for key in phonebook: 
        print(key," : ", phonebook[key])
    
def save_and_quit():
    with open('phonebook.pickle','wb') as filehandler:
        pickle.dump(phonebook, filehandler)
    print('Goodbye')
    
def tell_joke():
    print("What's the most important part of being a comedian?")
    time.sleep(5)
    print('timing')     
    time.sleep(1)   

menu = ['look up entry', 'set an entry', 'delete an entry', 'list all entries', 'quit and save', 'random joke']
       


while True: 
    print_menu()
    user_prompt = int(input('>> '))
    if user_prompt == 1:
        lookup_number()
    elif user_prompt == 2:
        set_entry()
    elif user_prompt == 3: 
        delete()
    elif user_prompt == 4: 
        list_all()
    elif user_prompt == 5:
        save_and_quit()    
        break
    elif user_prompt == 6:
        tell_joke()
 



