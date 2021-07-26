from DataParser import DataParser
import Ride
from User import User
import random



class Route:
    def __init__(self, rides):
        self.name = "Route"
        self.rides = rides
        self.path = []

    def displayRides(self):
        for ride in self.rides:
            ride.display()

    def generateRoute(self, showList):
        for ride in self.rides:
            for show in showList:
                if ride.movie == show:
                    self.path.append(ride)

    # def generateRoute(self, user):
    #     showList = user.showHistory
    #     for ride in self.rides:
    #         for show in showList:
    #             if ride.movie == show:
    #                 self.path.append(ride)

    def generateRoute(self, user):
        showList = user.showHistory

        for ride in self.rides:
            for show in showList:
                if ride.movie == show:
                    self.path.append(ride)


    def displayRoute(self):
        for ride in self.path:
            ride.display()











# fp = DataParser("Universal Data.csv")
# fp.findShows()
#
#
# route = Route(fp.rides)
# print(fp.showList)
#
#
#
# showsWatched = []
# showsWatched.append("Harry Potter")
# showsWatched.append("Shrek")
# showsWatched.append("The Cat in the Hat")
#
# patientZero = User("patientZero", showsWatched)
# route.generateRoute(patientZero)
# print(route.path)



