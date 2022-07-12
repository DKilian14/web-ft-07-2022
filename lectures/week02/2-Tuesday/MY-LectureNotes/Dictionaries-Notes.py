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
    
