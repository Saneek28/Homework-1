import math
from develop.src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        Figure.__init__(self, "triangle")
        self.a = a
        self.b = b
        self.c = c

    @property
    def area(self):
        half = self.perimeter / 2
        return math.sqrt(half * (half - self.a) * (half - self.b) * (half - self.c))

    @property
    def perimeter(self):
        return self.a + self.b + self.c
