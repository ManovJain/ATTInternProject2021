import random


class Ride:

    def __init__(self, name, year, movie, park, location, description):
        self.name = name
        self.year = year
        self.movie = movie
        self.park = park
        self.location = location
        self.description = description
        self.waitTime = self.waitTimeAnalyzer(self.waitTimeGenerator())

    def display(self):
        print(self.name)
        print(self.year)
        print(self.movie)
        print(self.park)
        print(self.location)
        print(self.description)

    def waitTimeGenerator(self):
        waitTime = random.randint(0, 3)
        return waitTime

    def waitTimeAnalyzer(self, i):
        if i == 1:
            return "short"
        elif i == 2:
            return "medium"
        elif i == 3:
            return "long"

    def addToMovieList(self, movies):  # this function checks to if the list that is passed in contains this ride's movie, if not it adds the movie to the list

        movie = self.movie
        if (movies.contains(movie) == False):
            movies.append(movie)
            return
        else:
            return

    def display(self):
        print(self.name)
        print("Description: ", self.description)
        print("Location: ", self.location)
        print("Wait Time: ", self.waitTime)
        print("Show/Movie: ", self.movie)
        print()
