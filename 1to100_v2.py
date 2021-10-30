# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:27:58 2020

Play number guessing game with Computer (secret number 1 to 100)

- Using a 'main' function
- Using sys library's exit function
- Using input function to get user input
- Using if function to make decisions

"""
# import libraries
import random
import sys

# set up a main function
# note that this only defines the function
# it does not run until it is called later in the code
def main():
    
    secret = random.randint(1,100)
    
    # print out the secret number
    print('Secret number is')
    print(secret)

# while True simply loops the code over and over again
# until told to exit
while True:
    
    # this actually tells the program to run 'main'
    # which we have coded to generate the secret number
    # and print it out
    main()
    
    # after running 'main', we use the input function
    # to decide whether to exit the loop
    user_input = input('Generate next number (y/n)? ')
    
    # now, we use the if function to check if user_input is 'n'
    # note '=' sign is used to assign a value to a variable
    # a '==' sign is used to check whether a variable is a certain value
    if user_input == 'n':
        sys.exit()