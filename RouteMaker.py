from DataParser import DataParser
import Ride

class Route:
    def __init__(self, rides):
        self.name = "Route"
        self.rides = rides


fp = DataParser("Universal Data.csv")

rides = fp.parse()
route = Route(rides)
route.rides[1].display()




