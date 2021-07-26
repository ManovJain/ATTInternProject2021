import Ride
from DataParser import DataParser
import RouteMaker
from RouteMaker import Route
from User import User


fp = DataParser("Universal Data.csv")
fp.findShows()


route = Route(fp.rides)
print(fp.showList)



showsWatched = []
showsWatched.append("Harry Potter")
showsWatched.append("Shrek")
showsWatched.append("The Cat in the Hat")

patientZero = User("Test User", showsWatched)
route.generateRoute(patientZero)



print("Hello welcome to the AT&T Parks and Rec Route Maker")

print("This is a User and his viewing history")
print(patientZero.name)
print(showsWatched)

print("Based on their viewing history, this is the path we have generated for them")
print(route.path)
