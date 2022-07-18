from develop.src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        Figure.__init__(self, "square")
        self.a = a

    @property
    def area(self):
        return self.a * self.a

    @property
    def perimeter(self):
        return 4 * self.a
