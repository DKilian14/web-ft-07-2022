zodiac = {
    "Aries": "The Warrior",
    "Taurus": "The Builder",
    "Gemini": "The Messenger",
    "Cancer": "The mother",
    "Leo": "The King",
    "Virgo": "The Analyst",
    "libra": "The Judge",
    "Scorpio": "The Magician",
    "Sagittarius": "The Gypsy",
    "Capricorn": "The Father",
    "Aquarius": "The Thinker",
    "Pisces": "The Mystic",
}

#  ---------------------- .get()

# zodiac.get("Aries") >>>>>>>>>>>>>>> will return "The Warrior"
# zodiac.get("NotInDictionary") >>>>>>>>>> will return None



# ------------------------- in
# "Aries" in zodiac >>>>>>>>>> will return True
# "NotInDictionary" in zodiac >>>>>>>>>> will return False


# ------------------------- .keys()
# zodiac.keys() >>>>>> will return >> dict_keys(['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'])

# --------------------------.values()
# zodiac.values() will return >> dict_values(['The Warrior', 'The Builder', 'The Messenger', 'The mother', 'The King', 'The Analyst', 'The Judge', 'The Magician', 'The Gypsy', 'The Father', 
# 'The Thinker', 'The Mystic'])


# ------------------------- del
# del zodiac["Aries"] will remove "Aries" from the deictionary. 

phonebook_dict = {
    'Alice': '703-493-1834',
    'Bob': '857-384-1234',
    'Elizabeth': '484-584-2923'
}

print(phonebook_dict['Elizabeth'])
phonebook_dict['Kareem'] = '938-489-1234'
del phonebook_dict['Alice']
phonebook_dict['Bob'] = '968-345-2345'


# --------------------------- iterating


# for key in zodiac: print(key," : ", zodiac[key])
#  ^^^^^^^ will return: 
    # Aries  :  The Warrior
    # Taurus  :  The Builder
    # Gemini  :  The Messenger
    # Cancer  :  The mother
    # Leo  :  The King
    # Virgo  :  The Analyst
    # libra  :  The Judge
    # Scorpio  :  The Magician
    # Sagittarius  :  The Gypsy
    # Capricorn  :  The Father
    # Aquarius  :  The Thinker
    # Pisces  :  The Mystic
    
ramit = {
    'name': 'Ramit',
    'email': 'ramit@gmail.com',
    'interests': ['movies', 'tennis'],
    'friends': [
        {
            'name': 'Jasmine',
            'email': 'jasmine@yahoo.com',
            'interests': ['photography', 'tennis']
        },
        {
            'name': 'Jan',
            'email': 'jan@hotmail.com',
            'interests': ['movies', 'tv']
        }
    ]
}

print(ramit['email'])
print(ramit['interests'][0])
print(ramit['friends'][0]['email'])
print(ramit['friends'][1]['interests'][1])