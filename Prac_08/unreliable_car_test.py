"""Testing program for unrealiable car
CP1404
Prac 08
"""

from unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("good car", 100, 90)
    bad_car = UnreliableCar("bad car", 100, 9)

    for i in range(1, 20):
        print("Attempting to drive {}km:".format(i))
        print("{:20} drove {}km".format(good_car.name, good_car.drive(i)))
        print("{:20} drove {}km".format(bad_car.name, bad_car.drive(i)))

    print(good_car)
    print(bad_car)


main()
