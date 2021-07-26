class Show:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def addScore(self):
        self.score = self.score + 1

    def display(self):
        str = self.name
        str = str + " " + self.score

        return str