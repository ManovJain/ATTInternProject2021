class Ride:
    def __init__(self, name, year,movie, park, location, description):
        self.name = name
        self.year = year
        self.movie = movie
        self.park = park
        self.location = location
        self.description = description

    def display(self):
        print(self.name)
        print(self.year)
        print(self.movie)
        print(self.park)
        print(self.location)
        print(self.description)

    def addToMovieList(self, movies):   #this function checks to if the list that is passed in contains this ride's movie, if not it adds the movie to the list

        movie = self.movie
        if(movies.contains(movie) == False):
            movies.append(movie)
            return
        else:
            return

