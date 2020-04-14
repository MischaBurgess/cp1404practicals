"""CP1404 - Guitar class."""
PRESENT_YEAR = 2020
VINTAGE_YEAR = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar class"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return Guitar information"""
        return "{} ({}) : ${:2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get Guitar age"""
        age = PRESENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Check if guitar is older than 50 years old (vintage)"""
        return self.get_age() >= VINTAGE_YEAR