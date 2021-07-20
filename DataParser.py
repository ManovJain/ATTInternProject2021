# importing csv module
import csv

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

        # printing the field names
        print('Field names are:' + ', '.join(field for field in fields))

        #  printing first 5 rows
        print('\nFirst 20 rows are:\n')
        for row in rows[:20]:
            # parsing each column of a row
            for col in row:
                print("%10s" % col),
            print('\n')


fp = DataParser("Universal Data.csv")
fp.parse()
