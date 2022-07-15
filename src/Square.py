from src.Figure import Figure


class Square(Figure):
    def __init__(self, a):
        Figure.__init__(self, "square")
        self.area = a ** 2
        self.perimeter = 4 * a


square = Square(2)
print("Площадь квадрата", square.area)
print("Периметр квадрата", square.perimeter)
