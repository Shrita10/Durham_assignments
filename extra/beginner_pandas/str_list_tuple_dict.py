# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:30:25 2020

@author: Shrita
"""

#String Functions
string = 'Hello. I am thinking of adding all the string functions  i encounter in this program'
string.upper()
string.lower()
string.isupper()
string.islower()
len(string)
string.index('f')
string.index('functions')
string.replace('encounter','get')
string.count('t')
string.endswith('m')
string.capitalize
string.casefold
string.center
string.isalnum
string.isalpha
string.isdecimal
string.zfill
string.swapcase
string.split
string.splitlines
string.startswith
str1 = ('tr','ma','dt')
x = ''.join(str1)
y = '#'.join(str1)
z = ' '.join(str1)
number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']
result = zip(number_list, str_list)
result_set = list(result)
print(result_set)
numbers = [2.5, 3, 4, -5]

numbers_sum = sum(numbers)
print(numbers_sum)

numbers_sum = sum(numbers, 10)
print(numbers_sum)

# vowels list
py_list = ['e', 'a', 'u', 'o', 'i']
print(sorted(py_list))

#function - map() passes each item of the iterable to this function.
numbers = (1, 2, 3, 4)
result = map(lambda x: x*x, numbers)
print(result)

# converting map object to set
numbersSquare = list(result)
print(numbersSquare)

vowels = ['a', 'e', 'i', 'o', 'u']
vowels_iter = iter(vowels)

print(next(vowels_iter))    # 'a'
print(next(vowels_iter))    # 'e'
print(next(vowels_iter))    # 'i'
print(next(vowels_iter))    # 'o'
print(next(vowels_iter))    # 'u'


grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)
  
num = 5
print(str(num))


import math
abs()
pow()
max()
min()
round()
math.floor()
math.ceil()
math.sqrt()



name  = input('whats your name')
