# -*- coding: utf-8 -*-
"""
Created on Sat May 25 13:47:46 2024

@author: Hafsa
"""
message = "Khulna University"
first_letter = message[0] # ‘K'
last_letter = message[-1] # ‘y’
print(first_letter, last_letter)

Sub_str = message[-4:-1]
print(Sub_str )    

S1 = message[-10] # ‘U’
S2 = message[-17] # ‘K’
print(S1, S2)

l=len(message)
print(l)
S2 = message[-l] # ‘y’
print("S2 is:  ",S2)


message = "Python_Class"
substring = message[1:6] # "ython" (extracts characters from index 1 to 6)
print(substring)


txt = "Smiling is a kind act and the Sunnah of our beloved Prophet Muhammad (PBUH)."
print(" Sunnah " in txt)     

print("expensive" not in txt)
print("Sunnah" not in txt)

find_txt = "expensive" not in txt
print("Is expensive in txt ? = ",find_txt)
