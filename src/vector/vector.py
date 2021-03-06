from math import hypot


class Vector:
    def __init__(self, x=0.0, y=0.0):
        self._x = float(x)
        self._y = float(y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.x == other.x and self.y == other.y

    def increment(self, other):
        self.x += other.x
        self.y += other.y

    def decrement(self, other):
        self.x -= other.x
        self.y -= other.y

    def sum(self, other):
        tmp = self

        tmp.x += other.x
        tmp.y += other.y
        return tmp

    def diff(self, other):
        tmp = self

        tmp.x -= other.x
        tmp.y -= other.y
        return tmp

    def vector_len(self):
        return hypot(self.x, self.y)

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = float(value)

    @y.setter
    def y(self, value):
        self._y = float(value)


if __name__ == "__main__":
    vector1 = Vector(7, 9)
    vector2 = Vector(4, 6)

    vector1.diff(vector2)

    print(vector1)
    print(vector2)
