import Ride
from DataParser import DataParser
import RouteMaker
from RouteMaker import Route
from User import User
import time
import random


fp = DataParser("Universal Data.csv")
fp.findShows()


route = Route(fp.rides)





# showsWatched = []
# showsWatched.append("Harry Potter")
# showsWatched.append("Shrek")
# showsWatched.append("The Cat in the Hat")
#
# patientZero = User("Test User", showsWatched)
# route.generateRoute(patientZero)



# print("Hello welcome to the AT&T Parks and Rec Route Maker")
#
#
# print()
# print()
#
# print("Here is a list of all available shows that can appear in a user's search history")
# print(fp.showList)
#
# yn = input("Would you like to generate a user?")
#
# print("This is a User and his viewing history:")
# print()
# print(patientZero.name)
# print(showsWatched)
#
# print()
# print()
#
# print("Based on their viewing history, this is the path we have generated for them")
# print()
# print()
# route.displayRoute()


class MenuManager():

    def runMenu(self):
        running = True
        while running == True:
           running = self.mainMenu()



    def mainMenu(self):
        print("Hello! Welcome to the AT&T Parks and Rec Path Generator")
        print("What would you like to see?")
        print("1. See all shows")
        print("2. See all Rides")
        print("3. Generate a User")
        print("4. Quit")
        print()

        i = input()
        return (self.option(i))

    def seeAllShows(self):
        print(fp.showList)
        print()
        print()

    def seeAllRides(self):
        print(route.displayRides())
        print()
        print()

    def createUser(self):
        print("Generating User...")
        # time.sleep(2)
        print("User Generated!")
        showsWatched = []
        showsWatched.append(random.choice(fp.showList))
        showsWatched.append(random.choice(fp.showList))
        showsWatched.append(random.choice(fp.showList))
        patientZero = User("Test User", showsWatched)

        patientZero.display()

        print("Would you like to see a generated route for this user? (yes/no)")
        i = input()

        if i == "yes":
            route.generateRoute(patientZero)
            route.displayRoute()
            return
        elif i == "no":
            return
        else:
            print("not a valid choice!")


    def option(self, userInput):
        if userInput == "1":
            self.seeAllShows()
            return True
        elif userInput == "2":
            self.seeAllRides()
        elif userInput == "3":
            self.createUser()
        if userInput == "4":
            return False


menu = MenuManager()
menu.runMenu()