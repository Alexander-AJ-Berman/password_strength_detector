#!/usr/bin/env python3

"""Strong Password Detector

This script allows the user to input a password and validate its strength. The criteria
for a strong password are as follows:

    1. At least 7 characters long
    2. Contains both uppercase and lowercase letters
    3. Contains at least one digit (0-9)
    4. Contains at least one special character (!, @, $)

There are no additional dependencies for the script other then Python3.

"""

#### Begin Script ####

import getpass
import re


pwd = getpass.getpass('Password: ')

# Can adjust requirements HERE
reqs = {
    'chars': 7, 
    'upper': 1, 
    'lower': 1, 
    'digit': 1, 
    'special': 1
    }

found = {
    'chars': 0, 
    'upper': 0, 
    'lower': 0, 
    'digit': 0, 
    'special': 0
    }



for char in pwd:

    # Increment total chars
    found['chars'] += 1

    # Increment alphabet chars
    if char.isalpha():
        # Increment upper
        if char.isupper():
            found['upper'] += 1
        # Increment lower
        else:
            found['lower'] += 1
    # Increment digits
    elif char.isdigit():
        found['digit'] += 1
    
    # Increment special chars
    else:
        found['special'] += 1

strong = True

# Check if conditions are met
for attr in found:
    if reqs[attr] > found[attr]:
        strong = False

if strong:
    print("Password is STRONG")
else:
    print("Password is WEAK")




    