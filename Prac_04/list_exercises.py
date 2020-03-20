"""Intermediate exercises"""
"1. Basic list operations"
numbers = []  # create empty list for numbers
for i in range(0, 5):  # ask for 5 numbers
    number_input = int((input("Number: ")))  # converts input to int
    numbers.append(number_input)  # appends input to list

print("The first number is", numbers[0])  # returns first number in list
print("The last number is", numbers[-1])  # returns last number in list
print("The smallest number is", min(numbers))  # returns smallest number in list
print("The largest number is", max(numbers))  # returns largest number in list
print("The average of the numbers is", sum(numbers) / len(numbers))  # returns average of all list elements


"2. Woefully inadequate security checker"
print("*2. Woefully inadequate security checker*")
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup',
             'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
             'InterpreterInterface', 'StartServer', 'bob']
username_input = input("Please enter your username: ")
if username_input in usernames: # check list for a match
    print("Access granted")
else:
    print("Access denied")
