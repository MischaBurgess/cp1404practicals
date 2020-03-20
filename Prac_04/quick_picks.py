""""Quick Pick" Lottery Ticket Generator"""
from random import randint # import random integer function
number_of_picks = int(input("How many quick picks would you like?: "))
max_number = int(45) # max number for picks
min_number = int(1) # minimum number for picks
max_length = int(6) # pick sequence max length


def main():
    for i in range(0, number_of_picks): # 0 to n picks
        pick_list = [] # create empty list
        for j in range(max_length): # for 1 - 6
            pick = randint(min_number, max_number) # generate random integers
            while pick in pick_list:
                pick = randint(min_number, max_number) # generate random integers
            pick_list.append(pick) # append random integers to list
        pick_list.sort() # sort list into ascending order
        print(" ".join("{:4}".format(pick) for pick in pick_list))
        # join lists with a spacing of 4 for every number in list


main()
