from .core import *


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        if type(other) == Vector2:
            self.x += other.x
            self.y += other.y
        elif type(other) == float or type(other) == int:
            self.x += other
            self.y += other
        else:
            print("Vector addition only supports vectors and scalars, not " + str(type(other)))

    def sub(self, other):
        if type(other) == Vector2:
            self.x -= other.x
            self.y -= other.y
        elif type(other) == float or type(other) == int:
            self.x -= other
            self.y -= other
        else:
            print("Vector subtraction only supports vectors and scalars, s not " + str(type(other)))


    def mul(self, k):
        self.x *= k
        self.y *= k

    def div(self, k):
        self.x /= k
        self.y /= k


    def __str__(self) -> str:
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def set(self, x, y):
        self.x = x
        self.y = y