from develop.src.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        Figure.__init__(self, "Rectangle")
        self.area = a * b
        self.perimeter = (a + b) * 2


rectangle = Rectangle(10, 20)
print("Площадь прямоугольника", rectangle.area)
print("Периметр прямоугольника", rectangle.perimeter)
