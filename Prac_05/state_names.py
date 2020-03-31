"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
Mischa Burgess
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":  # while state code is not empty
    if state_code.islower():  # checks if entered in lowercase
        state_code = state_code.upper()  # changes user input into uppercase
    if state_code in CODE_TO_NAME:  # if code matches, then..
        print(state_code, "is", CODE_TO_NAME[state_code])  # print description
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")

"""Part two"""

print("*Part Two: print list of states*")
for key, val in CODE_TO_NAME.items():  # for both key and values in dictionary
    print("{:3} is {:8}".format(key, val))  # print with correct spacing
