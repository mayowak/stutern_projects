#!/usr/bin/env python3
"""
Name: Mayowa Kolawole
Date: 06-11-2020
Purpose: display information about a person
"""

def meet_user():
    Name = input("What is your name?")  # To get the User name
    Age = input("How old are you?")  # To get the user age
    Gender = (input("Are you a male? (True/False)"))  # To get the User gender

    # To generate the conditions for calling out the Gender parameter
    if 'T' in Gender:
        print(f"Hello, Mr. {Name}, you are {Age} years old.")
    else:
        print(f"Hello, Mrs. {Name}, you are {Age} years old.")

    age = int(Age)
    DOB = 2020 - age  # To get the user date of birth
    print(f"You were born in the year {DOB}.")

    # To Generate the conditions for age grouping
    user_age = float(Age)
    if user_age < 1:
        print(f"you are an infant.")
    elif user_age <= 12:
        print(f"you are a child.")
    elif user_age <= 19:
        print(f"you are a teen.")
    elif user_age == 20<=65:
        print(f"you are an adult.")
    elif user_age >= 65:
        print(f"you are an elderly person.")
    else:
        print("Unreal input.")

    # To calculate the user age a decade ago
    decade = age - 10
    print(f"A decade ago you were {decade} years old.")

    # To get the users age for the next 50 years
    current_year = age + 10
    print(f"In 2030 you'll be {current_year} years old.")

    current_year = age + 20
    print(f"In 2040 you'll be {current_year} years old.")

    current_year = age + 30
    print(f"In 2050 you'll be {current_year} years old.")

    current_year = age + 40
    print(f"In 2060 you'll be {current_year} years old.")

    current_year = age + 50
    print(f"In 2070 you'll be {current_year} years old")


# Calling out the greet_user function
meet_user()