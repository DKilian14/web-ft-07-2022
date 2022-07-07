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


# matrix1 = [[1,3],[2,4],[1,1]]
# matrix2 = [[5,2],[1,0],[1,1]]
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

# leet_alphabet = [["a","4"],["e","3"],["g","6"],["i","1"],["o","0"],["s","5"],["t","7"]]
# statement = list(input('Write a statement: ').lower())
# statement_index = 0


# while statement_index < len(statement):
#     leet_index = 0
    
#     while leet_index < len(leet_alphabet):
        
#         if leet_alphabet[leet_index][0] == statement[statement_index]:
#             statement[statement_index] = leet_alphabet[leet_index][1]
            
#         leet_index +=1

    

#     statement_index +=1
# statement = ''.join(statement)
# print(statement)

############################## 6. Long-long Vowels

# Given a word as a string, print the result of extending any long vowels to the length of 5. 

# Examples:

# ```
# Good => Goooood 
# Cheese => Cheeeeese 
# Man => Man 
# Spoon => Spooooon 
# ```

# --------------------------------ANSWER---------------------------------

# vowels = ['a','e','i','o','u']
# word = list(input('Provide a word:  '))
# word_index = 0

# while word_index < len(word):
#     vowel_index = 0
#     while vowel_index < len(vowels):
#         if vowels[vowel_index] == word[word_index]:
#             word[word_index] = word[word_index]*5
#         vowel_index +=1
#     word_index += 1

# print("".join(word))

################################################# 7. Caesar Cipher

# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? [Learn about it here](http://practicalcryptography.com/ciphers/caesar-cipher/).

# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"


# ---------------------------ANSWER-----------------------------------


# iterate through the message 
# #check each letter
####iterate through the key [[a,b],[b,c]]
######if there is a match, change the value of the character of the message to the corresponding value in the key. 

# message = list(input('Enter your super secret message: '))
# key = [['a','k'],['b','l'],['c','m'],['d','n'],['e','o'],['f','p'],['g','q'],['h','r'],['i','s'],
#        ['j','t'],['k','u'],['l','v'],['m','w'],['n','x'],['o','y'],['p','z'],['q','a'],['r','b'],
#        ['s','c'],['t','d'],['u','e'],['v','f'],['w','g'],['x','h'],['y','i'],['z','j']]

# message_index = 0

# while message_index < len(message):
#     key_index = 0
#     while key_index < len(key):
#         print(message)
#         print(message[message_index])
#         if key[key_index][0] == message[message_index]:
#             message[message_index] = key[key_index][1]
#             # stop the < while key_index < len(key): > loop
#             key_index = len(key)
#         key_index +=1
#     message_index +=1
    
# print(message)

################################################# 7.1 Caesar Cipher (cont.)
# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

# message = list('lbh zhfg hayrnea jung lbh unir yrnearq')
            
# key = [['a','n'],['b','o'],['c','p'],['d','q'],['e','r'],['f','s'],['g','t'],['h','u'],['i','v'],
#        ['j','w'],['k','x'],['l','y'],['m','z'],['n','a'],['o','b'],['p','c'],['q','d'],['r','e'],
#        ['s','f'],['t','g'],['u','h'],['v','i'],['w','j'],['x','k'],['y','l'],['z','m']]

# message_index = 0

# while message_index < len(message):
#     key_index = 0
#     while key_index < len(key):
#         # print(message)
#         # print(message[message_index])
#         if key[key_index][1] == message[message_index]:
#             message[message_index] = key[key_index][0]
#             # stop the < while key_index < len(key): > loop
#             key_index = len(key)
#         key_index +=1
#     message_index +=1
    
# print(''.join(message))


## Large 

### Matrix Multiplication
# Given two two-dimensional lists of numbers of the size 2x2 - calculate the result of multiplying the two matrices. Print the resulting matrix.

matrix1 = [[2,1],
           [0,3]]

matrix2 = [[4,2],
           [1,5]]

product=[[0,0],
         [0,0]]

#iterate through rows of matrix1
#iterate through columns of matrix2
#iterate through rows of matrix2

matrix1_row = 0
while matrix1_row < len(matrix1):
    matrix2_column = 0
    while matrix2_column < len(matrix2[0]):
        matrix2_row = 0
        while matrix2_row < len(matrix2):
            product[matrix1_row][matrix2_column] += matrix1[matrix1_row][matrix2_row] * matrix2[matrix2_row][matrix2_column]
            
            matrix2_row +=1
        matrix2_column+=1
    matrix1_row+=1

print("answer should be <[[9, 9], [3, 15]] > ")

print(product)

# How do you multiple two matrices?

