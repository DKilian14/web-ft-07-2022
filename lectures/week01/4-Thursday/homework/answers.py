# Homework
## Iterative Programming

#### 1. Multiply Vectors

# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:

# ```
# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]
# ```

list1 = [2,4,5]
list2 = [2,3,6]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i]*list2[i])


print(list3)