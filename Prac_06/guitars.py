"""CP1404 - Guitar Collection Task."""

from guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print("{} ({}): {} added.".format(name, year, cost))
        guitar_adding = Guitar(name, year, cost)
        name = input("Name: ")
        guitars.append(guitar_adding)
    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Other Guitar", 2010, 1000.00))

    if guitars != "":
        print("These are my guitars: \n")
        i = 0
        for i, guitar in enumerate(guitars):
            vintage = ""
            if guitar.is_vintage():
                vintage = "(Vintage)"
            print("Guitar {}: {} ({}), worth $ {} {}".format(i + 1, guitar.name, guitar.year, guitar.cost, vintage))


main()
