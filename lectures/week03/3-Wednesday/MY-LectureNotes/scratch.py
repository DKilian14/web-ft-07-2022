
# create a loop that counts from 100 to 0 by increments of 5.

# for example
# 100, 95, 90, 85 ...
# Do with a for loop first then with a while loop

for i in range(0,100,5):
    print(100-i)
    
count = 100


print('ROUND 2')

while count >0:
    print(count)
    count-=5
    
print('ROUND 3')

def countdown(num):
    if num == 0:
        return 0
    else:
        print(num)
        return countdown(num-5)
    
print(countdown(100))


# in the dictionary below, extract the following 
# first_name 
# last_name 
# user's employement title 
# user's key_skills
# user's street address
# user's city 
# user's credit card number 
# user's subscription plan
user = {
    
    
    "id": 5487,
    "uid": "7b98255c-be80-483e-a508-1edbc9ffcc58",
    "password": "vtN0KSaejW",
    "first_name": "Regina",
    "last_name": "O'Keefe",
    "username": "regina.o'keefe",
    "email": "regina.o'keefe@email.com",
    "avatar": "https://robohash.org/anihilexcepturi.png?size=300x300&set=set1",
    "gender": "Genderfluid",
    "phone_number": "+240 441.465.1205 x2861",
    "social_insurance_number": "471267534",
    "date_of_birth": "1964-08-23",
    "employment": {
        "title": "Forward Consulting Producer",
        "key_skill": "Networking skills"
    },
    "address": {
        "city": "West Rivabury",
        "street_name": "Kassulke Key",
        "street_address": "63277 Sarita Neck",
        "zip_code": "06366",
        "state": "Illinois",
        "country": "United States",
        "coordinates": {
        "lat": -11.987728561637226,
        "lng": -124.02257039722036
    }
    },
    "credit_card": {
        "cc_number": "5228-8351-1376-5139"
    },
    "subscription": {
        "plan": "Professional",
        "status": "Active",
        "payment_method": "Google Pay",
        "term": "Annual"
    }
}

print(user['first_name'])
print(user['last_name'])
print(user['employment']['title'])
print(user['employment']['key_skill'])
print(user['address']['street_address'])
print(user['address']['city'])
print(user['credit_card']['cc_number'])
print(user['subscription']['plan'])

