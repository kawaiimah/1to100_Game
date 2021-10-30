# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:27:58 2020

Play number guessing game with Computer (secret number 1 to 100)

- Using variables
- Using random library's randint function
- Using print function to output information to the display

"""

# load the random library which contains various functions
# relating to random numbers
import random

# set up a variable called secret, use the randint function to
# assign to it a random integer between 1 and 100 (inclusive)
secret = random.randint(1,100)

# print out the secret number
print('Secret number is')
print(secret)

# run this program multiple times to see that with each run
# a different random integer is chosen for secret