# -*- coding: utf-8 -*-
"""
Created on Sat May 25 14:43:49 2024

@author: Hafsa
"""

my_str = "      Helping others is a Sunnah  "

# upper(): Convert to uppercase 
print(my_str.upper())

#lower(): Convert to lowercase 
print(my_str.lower())

print(my_str.title())

#strip(): Remove leading and trailing whitespaces 
#print(my_str.strip(" "))
print(my_str.strip())
print(my_str.rstrip(), my_str)
#find(substring): Find the index of the first occurrence of a substring (returns -1 if not found).
print(my_str.find("Sunnah"))    #22
print(my_str.find("Helping"))   #2

#replace(old, new): Replace all occurrences of a substring with another substring.
print(my_str.replace("Helping","Supporting"))   #Supporting others is Sunnah.

#count()	Returns the number of times a specified value occurs in a string
print(my_str.count("i"))  #2


my_str = "Helping others is a Sunnah"
#split()
print(my_str.split(" "))


