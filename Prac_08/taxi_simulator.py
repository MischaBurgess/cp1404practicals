"""
Taxi simulator using Taxi class
CP1404 Practical
Prac 08
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print("Let's drive!")
    print(MENU)
    total_bill = 0
    user_choice = input(">>> ")
    while user_choice.lower() != "q":
        if user_choice.lower() == "c":
            display_available_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice]
            print("Bill to date: ${:.2f}".format(total_bill))
        elif user_choice.lower() == "d":
            taxi_cost = drive_taxi(current_taxi)
            total_bill += taxi_cost
            print("Bill to date: ${:.2f}".format(total_bill))
        else:
            print("Invalid menu option")
        print(MENU)
        user_choice = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")
    display_available_taxis(taxis)


def drive_taxi(current_taxi):
    drive_length = float(input("Drive how far?: "))
    current_taxi.start_fare()
    current_taxi.drive(drive_length)
    taxi_cost = current_taxi.get_fare()
    print("Your {} trip will cost you ${:.2f}".format(current_taxi.name, taxi_cost))
    return taxi_cost


def display_available_taxis(taxis):
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


main()
