# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:13:45 2024

@author: Hafsa
"""

'''
# Step 1: Initialize the strings
str1 = input("Enter First String: ")  #Hello
str2 = input("Enter Second String: ")  #World

# Step 2: Remove the first character from each string
str1_sliced = str1[1:]  # "ello"
str2_sliced = str2[1:]  # "orld"

# Step 3: Concatenate the sliced strings
result = str1_sliced + str2_sliced  # "ello" + "orld" = "elloworld"

# Step 4: Print the result
print(result)  # Output: "elloworld"

'''
'''

# Take user input for num1 and num2
num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))

# Check if the numbers are equal
if num1 == num2:
    result = 2 * (num1 + num2)
else:
    result = num1 + num2

# Print the result
print("The result is:", result)

'''
'''
# Step 1: Take user input for the tag and the word
tag = input("Enter the tag: ")
word = input("Enter the word: ")

# Step 2: Construct the HTML tag
result = '<' + tag + '>' + word + '</' + tag + '>'

# Step 3: Print the result
print(result)
'''


#lec -8
for num in range(1, 11):
    print(num, "squared is", num * num)