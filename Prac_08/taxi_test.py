"""Taxi class tester
CP1404 practical
prac 08
"""
from taxi import Taxi


def taxi_test():
    new_taxi = Taxi("Prius 1", 100)  # new taxi with 100 units of fuel @ $1.23
    new_taxi.drive(40) # drive 40km
    print(new_taxi)
    new_taxi.start_fare() # start new fare
    new_taxi.drive(100) # drive 100km
    print(new_taxi)


taxi_test()
