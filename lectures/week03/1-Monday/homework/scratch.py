# nums = [2,7,11,15]
# target = 9

# for i in range(len(nums)): #iterate through each number
#     if nums[i] < target: #if the number is less than taget:
#         for j in range(i+1,len(nums)): #iterate through each number starting with the number at index of [i+1]
#             if nums[j]+nums[i]==target:  # if num1 and num2 are equal to the target:  
#                 ans= [i,j] #initialize the answer.
    
# print(ans)

# 1. Determine the total distance travelled and the
# total time it takes to get there by summing up
# the total distance and the total time in the list below

# trips = [
#     { "distance": 34, 'time': 10 },
#     { "distance": 90, 'time': 50 },
#     { "distance": 59, 'time': 25 },
#     { "distance": 83, 'time': 60 },
#     { "distance": 27, 'time': 15 },
#     { "distance": 68, 'time': 90 }
# ]


# distance_sum = 0
# time_sum = 0
# for i in trips:
#     distance_sum += i['distance']
#     time_sum += i['time']
    
    
# print(f"total distance = {distance_sum}. Total time = {time_sum}")


# 2. Implement a 'pluck' function. 
# Pluck should accept a list and a string representing a 
# property name and return a list containing that property from each object.

# example
# paints = [{"color": 'red', "text-align": "right"}, {"color": 'blue', "margin": "0px"}, {"color": 'yellow', "padding": "5px"}]
# pluck(paints, 'color')
# returns =>>>>> ['red', 'blue', 'yellow']

# paints = [{"color": 'red', "text-align": "right"}, {"color": 'blue', "margin": "0px"}, {"color": 'yellow', "padding": "5px"}]


# def pluck(paints, color):
#     values = []
#     for i in paints:
#         values.append(i[color])
#     print(values)
    
# pluck(paints, 'color')