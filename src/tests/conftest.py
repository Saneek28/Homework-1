import pytest

from develop.src.Circle import Circle
from develop.src.Rectangle import Rectangle
from develop.src.Square import Square
from develop.src.Triangle import Triangle


@pytest.fixture(scope='class')
def triangle():
    return Triangle(14, 13.5, 5)


@pytest.fixture(scope='class')
def rectangle():
    return Rectangle(14, 5)


@pytest.fixture(scope='class')
def square():
    return Square(5.3)


@pytest.fixture(scope='class')
def circle():
    return Circle(9.1)
