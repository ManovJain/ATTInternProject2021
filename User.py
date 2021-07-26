class User:
    def __init__(self, name,  showHistory):
        self.name = name
        self.showHistory = showHistory #this is a list of shows watched by the user

    def display(self):
        print(self.name)
        print(self.showHistory)




# showsWatched = []
# showsWatched.append("Harry Potter")
# showsWatched.append("Shrek")
# showsWatched.append("The Cat in the Hat")
#
# patientZero = User("patientZero", showsWatched)