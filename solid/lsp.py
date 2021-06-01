'''
Design Prinicples were introduced by Robert C. Martin
SOLID is just a selection of 5 principles of many many others.
These are frequently refered to in modern programming &
apply directly to design patterns

Liskov Substitution Principle
If you have a base class, any interface using it such as functions, methods 
Should function correctly on any derived classes of the base class.
'''
class Rectangle:
    def __init__(self, width, height) -> None:
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self) -> str:
        return f'Width: {self.width}, Height: {self.height}'


    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value


class Square(Rectangle):
    def __init__(self, size) -> None:
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value

# This breaks the liskov principle, because rc.height is set
# So our derived class square cannot this function correctly
# so use_it only works on a Rectangle and not a derived class aka Square
def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f'expected an area of {expected}, got {rc.area}')

rc = Rectangle(2,3)
use_it(rc)

sq = Square(5)
use_it(sq)