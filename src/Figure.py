class Figure():
    def __init__(self, name):
        self.name = name

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return figure.area + self.area
        else:
            raise ValueError
