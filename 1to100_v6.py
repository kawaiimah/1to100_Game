# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 21:27:58 2020

Play number guessing game with Computer (secret number 1 to 100)

- Finally, let's allow the player to keep guessing until correct
- Included a counter to keep count of how many tries!

"""

import random
import sys

def main():
    
    secret = random.randint(1,100)
    counter = 0
    correct = False
    
    # this is the main loop that keeps going until
    # the player gets it correct
    while (correct == False):
        
        #############################################################
        # This code section obtains player input
        
        # use valid as a flag whether a valid input has been received
        valid = False
        
        while (valid == False):
        
            # ask player for a guess
            guess_string = input('Your guess [1-100, "q" to quit]? ')
            
            # assume input is valid for the moment
            # we can change it back to invalid via the checks
            valid = True
            
            # check if input is 'q'
            if guess_string == 'q':
                sys.exit()
        
            # check if input is numeric integer and between 1 and 100
            if (guess_string.isnumeric() == False):
                print('Invalid input!')
                valid = False
            else:
                guess = int(guess_string)
                if ((guess < 1) or (guess > 100)):
                    print('Please guess a number from 1 to 100!')
                    valid = False
        #############################################################
        
        # now that a valid input is received, increase the counter
        counter = counter + 1
     
        # check if bigger or smaller, set correct to True if right
        if guess < secret:
            print('My secret number is bigger than that!')
        elif guess > secret:
            print('My secret number is smaller than that!')
        else:
            print('You got it right!')
            correct = True
        
    # print out the secret number and number of tries
    print('My secret number is', secret)
    print('You took', counter, 'tries!')


while True:
    
    main()

    user_input = input('Generate next number (y/n)? ')
    
    if user_input == 'n':
        sys.exit()