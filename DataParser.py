# importing csv module
import csv
from Ride import Ride
import Show

class DataParser:
    def __init__(self, filename):
        self.filename = filename
        self.potterRides = []
        self.rides = self.parse()
        self.showList = []

    def parse(DataParser):
        # csv file name

        # initializing the titles and rows list
        fields = []
        rows = []

        # reading csv file
        with open(DataParser.filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # get total number of rows
            # print("Total no. of rows: %d" % (csvreader.line_num))

            rides = []

            for row in rows:
                name = row[0]
                year = row[1]
                movie = row[2]
                park = row[3]
                location = row[4]
                description = row[5]

                ride = Ride(name, year, movie, park, location, description)
                rides.append(ride)

            return rides

    def findShows(self):
        for ride in self.rides:
            if ride.movie in self.showList:
               # print("Already exists")
                print()
            else:
                self.showList.append(ride.movie)


    def findPotterRides(self):

        for ride in self.rides:
           if "Harry Potter" in ride.movie:
            self.potterRides.append(ride)

        for potterRide in self.potterRides:
            print(potterRide.name)




