"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()


def fahrenheit_to_celsius(fahrenheit):
    result = float(5.0 / 9.0 * (fahrenheit - 32.0))
    return result


def celsius_to_fahrenheit(celsius):
    result = float(celsius * 9.0 / 5.0 + 32.0)
    return result


while choice != "Q":
    if choice == "C":
        celsius = float(input("Enter a value to convert: "))
        print("The converted value is: {0:.2f} fahrenheit".format(celsius_to_fahrenheit(celsius)))
    elif choice == "F":
        fahrenheit = float(input("Enter a value to convert: "))
        print("The converted value is: {0:.2f} celsius".format(fahrenheit_to_celsius(fahrenheit)))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
