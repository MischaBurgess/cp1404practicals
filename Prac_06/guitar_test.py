"""CP1404 - Guitar testing program."""

from guitar import Guitar
PRESENT_YEAR = 2020


def test_guitars():
    name1 = "Gibson L-5 CES"
    year1 = 1922
    cost1 = 16035.40
    name2 = "Other guitar"
    year2 = 2010
    cost2 = 1000.00
    guitar1 = Guitar(name1, year1, cost1)
    guitar2 = Guitar(name2, year2, cost2)
    print("{} get_age() - Expected 98. Got {}".format(guitar1.name, guitar1.get_age()))
    print("{} get_age() - Expected 10. Got {}".format(guitar2.name, guitar2.get_age()))
    print("{} is_vintage() - Expected True. Got {}".format(guitar1.name, guitar1.is_vintage()))
    print("{} is_vintage() - Expected False. Got {}".format(guitar2.name, guitar2.is_vintage()))


test_guitars()
