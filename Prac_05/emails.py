"""
Emails Task
Mischa Burgess
"""


def main():
    # global name, email
    name_from_email = {}  # create empty dictionary
    email = input("Email: ")
    while email != "":  # while email is not empty
        name = email_to_name_function(email)  # get name from email using function
        response = input("Is your name {}? (y/n) ".format(name))  # check name is correct
        if response.lower() != "y" and response != "":  # is response is 'n'
            name = input("Name: ")
        name_from_email[email] = name  # save name in dictionary
        email = input("Email: ")
print("\n")  # print new line
    for email, name in name_from_email.items():  # iterate through dictionary (both keys and values)
        print(" {} ({})".format(name, email))  # print results


def email_to_name_function(email):
    # global email, name_from_email, name
    email_split = email.rsplit("@")  # splits all following '@'
    email_split.pop(1)  # deletes everything after '@'
    name_parts = email_split[0].split(".")  # split the name after the '.'
    name = " ".join(name_parts).title()  # capitalise name & attach names
    return name


main()