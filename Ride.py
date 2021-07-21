class Ride:
    def __init__(self, name, year, manufacturer, park, location, description):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.park = park
        self.location = location
        self.description = description

    def fillData(self, rows):

        rides = []

        for row in rows:
            print(row)
            print("row")
            name, year, manufacturer, park, location, description = row.split(', ')
            ride = Ride(name, year, manufacturer, park, location, description)
            rides.append(ride)
            print(ride)


