"""
Tests Silver Service Taxi class
CP1404 practical
Prac 08
"""

from silver_service_taxi import SilverServiceTaxi


def silver_service_taxi_test():
    silver_taxi = SilverServiceTaxi("silver_taxi", 100, 2)
    silver_taxi.drive(18)
    print(silver_taxi)
    print("Fare = ${:.2f}".format(silver_taxi.get_fare()))


silver_service_taxi_test()
