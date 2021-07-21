class Ride:
    def __init__(self, name, year, manufacturer, park, location, description):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.park = park
        self.location = location
        self.description = description

    def display(self):
        print(self.name)
        print(self.year)
        print(self.manufacturer)
        print(self.park)
        print(self.location)
        print(self.description)