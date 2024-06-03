# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 01:21:38 2024

@author: Hafsa
"""
def love6(a, b):
  sum_ab=a+b
  sub_ab=abs(a-b)
  if sum_ab==6 or sub_ab==6 or a==6 or b==6:
    return True
  else:
    return False


def non_start(a, b):
  return (a[1:len(a)]+b[1:len(b)])


def sum_double(a, b):
  if a==b:
    sum=2*(a+b)
  else:
    sum=a+b
  return(sum)


def make_tags(tag, word):
  return('<'+tag+'>'+word+'</'+tag+'>')
