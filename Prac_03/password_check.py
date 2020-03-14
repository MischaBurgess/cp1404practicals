"""Created by Mischa Burgess"""
"""Password checker"""
"""Checks the length of password and returns asterisks"""

def main():
    password = get_password()
    print_stars(password)


def print_stars(password):
  for i in range(0, len(password)):
    print("*", end=' ')  ## print asterisks


def get_password():
  min_length = 10
  password = input("Please enter a password with at least {} characters: ".format(min_length))
  while len(password) < min_length:
    password = input("Please enter a password with at least {} characters: ".format(min_length))
  return password


main()
