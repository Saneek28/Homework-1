class Figure():
    def __init__(self, name):
        self.name = name

    def add_area(self, figure):
        return self.area + figure.area
