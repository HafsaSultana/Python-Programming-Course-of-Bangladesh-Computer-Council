# -*- coding: utf-8 -*-
"""
Created on Sat May 25 16:01:36 2024

@author: Hafsa
"""
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)

a = 10
b = 20
c=b/a
list1 = [1, 2, 3, 4, 5 ]

print ("a: ", a, "b: ", b, "c: ", c, "list1:", list1)

print( a in list1)
print( b not in list1)
print( c in list1)

#1
input_string = "hello"
reversed_string = input_string[::-1]
print(reversed_string)  # Output: "olleh"

#2
input_string = "racecar"
is_palindrome = input_string == input_string[::-1]
print(is_palindrome)  # Output: True

#4
input_string = "apple,banana,orange"
split_list = input_string.split(',')
print(split_list)  # Output: ["apple", "banana", "orange"]

