# importing csv module
import csv
from Ride import Ride

class DataParser:
    def __init__(self, filename):
        self.filename = filename

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
            print("Total no. of rows: %d" % (csvreader.line_num))

            rides = []

            for row in rows:
                name = row[0]
                year = row[1]
                manufacturer = row[2]
                park = row[3]
                location = row[4]
                description = row[5]

                ride = Ride(name, year, manufacturer, park, location, description)
                print(ride)
                rides.append(ride)

            return rides

        #     # printing the field names
        # print('Field names are:' + ', '.join(field for field in fields))
        #
        # #  printing first 5 rows
        # print('\nFirst 20 rows are:\n')
        # for row in rows[:20]:
        #     # parsing each column of a row
        #     for col in row:
        #         print("%10s" % col),
        #     print('\n')



fp = DataParser("Universal Data.csv")
fp.parse()
