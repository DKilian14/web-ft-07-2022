# Return a new list with each element multiplied by 5

nums = [56, 34, 34, 1, 1, 1, 23, 12, 89, 89, 89, 70, 56] 

for i in range(len(nums)):
    nums[i] = nums[i]*5

print(nums)
# Given a list [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this {'job': 'Instructor', 'name': 'Elie'} (the order does not matter).

info = [("name", "Elie"), ("job", "Instructor")]
info_dict = {}

for i in info:
    info_dict[i[0]] = i[1]
    
print(info_dict)