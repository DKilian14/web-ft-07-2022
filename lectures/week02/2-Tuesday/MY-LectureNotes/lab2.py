import corona




# 1.1Make it look like:
#    State
#   Address (street, suite, city, zipcode)

# 1.2Find the sum of all recovered cases

corona_data = corona.data

for key in corona_data:
    print(key)
    
# get the name of the state for every item