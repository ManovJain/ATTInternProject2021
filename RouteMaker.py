import DataParser


class Route:
    def _init_(self, name, year, manufacturer, park, location, description):
        self.name = name
        self.year = year
        self.manufacturer = manufacturer
        self.park = park
        self.location = location
        self.description = description

fp = DataParser("Universal Data.csv")
fp.parse()

