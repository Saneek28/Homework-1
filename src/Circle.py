import math

from src.Figure import Figure


class Circle(Figure):
    def __int__(self, radius):
        Figure.__init__(self, "circle")
        self.area = math.pi * radius ** 2
        self.perimeter = 2 * math.pi * radius


radius = 2
circle = Circle(radius)
print('Площадь окружности с радиусом 2 равна:', math.pi * (radius ** 2))
print('Периметр окружности с радиусом 2 равна:', 2 * math.pi * radius)
