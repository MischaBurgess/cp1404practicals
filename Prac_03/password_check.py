"""Created by Mischa Burgess"""
"""Password checker"""
"""Checks the length of password and returns asterisks"""

print("Your password should have a minimum length of 10 characters")
password = input("Please enter your password: ")
min_length = 10 ## minimum character length
if len(password) < min_length:
  print("Your {} character password is invalid".format(len(password)))
elif len(password) > min_length:
  for i in range(0, len(password)):
    print("*", end=' ') ## print asterisks