# Homework
## Iterative Programming

############################## 1. Multiply Vectors

# Given two lists of numbers of the same length, create a new list by multiplying the pairs of numbers in corresponding positions in the two lists. Example:

# ```
# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]
# ```

# --------------------ANSWER----------------------

# list1 = [2,4,5]
# list2 = [2,3,6]
# list3 = []

# for i in range(len(list1)):
#     list3.append(list1[i]*list2[i])
# print(list3)

############################## 2. Matrix Addition

# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented as an list of lists:

# ```
# [ [2, -2],
#    [5, 3] ]
# ```

# Calculate the result of adding the two matrices. The number in each position in the resulting matrix should be the sum of the numbers in the corresponding addend matrices. Example: to add
# ```
# 1 3
# 2 4
# ```
# and
# ```
# 5 2
# 1 0
# ```
# results in
# ```
# 6 5
# 3 4
# ```

#------------------ ANSWER----------------------

# matrix1 = [[1,3],[2,4]]
# matrix2 = [[5,2],[1,0]]
# matrix3 = [[],[]]

# for i in range(len(matrix1)):
#     for j in range(len(matrix1[i])):
#         matrix3[i].append(matrix1[i][j] + matrix2[i][j])
        
# print(matrix3)


####################### 3. Matrix Addition II

# Use your solution in Matrix Addition, and extend it to work for a pair of matrices of any size, as long as they have the same size.

# ---------------------------ANSWER-----------------------------------------


# matrix1 = [[1,3],[2,4]]
# matrix2 = [[5,2],[1,0]]
# matrix3 = []

# for i in range(len(matrix1)):
#     matrix3.append([])
#     for j in range(len(matrix1[i])):
#         matrix3[i].append(matrix1[i][j] + matrix2[i][j])
        
# print(matrix3)

############################ 4. De-dup

# Given a list of numbers or strings, create a new list containing the same elements as the first list, except with any duplicate values removed. Print the list.

# --------------------------ANSWER------------------

# list = [1,'bob',1,'steve','bob', 24, 13, 24]
# no_duplicate_list = []

# while len(list):
#     value_to_check = list[0]
#     if value_to_check in no_duplicate_list:
#         # print('there are duplicates of this value', value_to_check)
#         pass
#     else:
#         no_duplicate_list.append(value_to_check)
#     list.pop(0)
    
# print(no_duplicate_list)


############################# 5. Leetspeak

# Given a paragraph of text as a String, print the paragraph in [leetspeak](https://en.wikipedia.org/wiki/Leet). 

# To translate a String to leetspeak, you need to replace make the following character replacements (treat all input characters as uppercase):

# | Letter | Translates To |
# |:------:|:-------------:|
# | A      | 4             |
# | E      | 3             |
# | G      | 6             |
# | I      | 1             |
# | O      | 0             |
# | S      | 5             |
# | T      | 7             |

# Example: If your program is given the String `"I am a leet programmer"`, it should print `"1 4m 4 l337 pr0gr4mm3r"` as the leetspeak translation


# --------------------------------ANSWER------------------------------

leet_alphabet = [[a,4],[e,3],[g,6],[i,1],[o,0],[s,5],[t,7]]