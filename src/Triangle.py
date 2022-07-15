from src.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c):
        Figure.__init__(self, "triangle")
        self.area = 1 / 2 * a * b
        self.perimeter = a + b + c


triangle = Triangle(2, 13, 14, )
print("Площадь треугольника", triangle.area)
print("Периметр треугольника", triangle.perimeter)
