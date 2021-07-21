from DataParser import DataParser
from Ride import Ride

class Route:
    def _init_(self, rides):
        self.name = "Route"
        rides = rides

    def fillData(self, rows):
        rides = []

        for row in rows:
            name, year, manufacturer, park, location, description = row.split(', ')
            ride = Ride(name, year, manufacturer, park, location, description)
            rides.append(ride)
            print(ride)

fp = DataParser("Universal Data.csv")

route = Route(fp.parse())




