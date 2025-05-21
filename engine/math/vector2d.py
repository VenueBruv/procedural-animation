from . import sqrt, sin, cos, degrees, radians, atan2

class Vector2D:
    def __init__(self, x=0, y=0):
        self._x = round(x, 5)
        self._y = round(y, 5)

    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def from_other(self, other):
        return self - other
    
    def to_other(self, other):
        return other - self

    def normal(self):
        return Vector2D(-self.y, self.x)

    def normalize(self):
        return self / self.magnitude

    @classmethod
    def from_angle(cls, angle):
        x = round(cos(radians(angle)), 5)
        y = round(sin(radians(angle)), 5)
        return cls(x, y)
    
    @property
    def direction(self):
        return degrees(atan2(self.y, self.x))
    
    @property
    def magnitude(self):
        return sqrt(self.x**2 + self.y**2)

    @property
    def pos(self):
        return (self.x, self.y)
    
    @pos.setter
    def pos(self, value):
        self.x, self.y = value
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        self._x = round(value, 5)

    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        self._y = round(value, 5)

    def __repr__(self):
        return f'{self.pos}'
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)
    
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self
    
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector2D(x, y)
    
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self
    
    def __mul__(self, other):
        if type(other) == Vector2D:
            x = self.x * other.x
            y = self.y * other.y
            return Vector2D(x, y)
        
        x = self.x * other
        y = self.y * other
        return Vector2D(x, y)
    
    def __imul__(self, other):
        if type(other) == Vector2D:
            self.x *= other.x
            self.y *= other.y
            return self
        
        self.x *= other
        self.y *= other
        return self
    
    def __truediv__(self, other):
        try:
            if type(other) == Vector2D:
                x = self.x / other.x
                y = self.y / other.y
                return Vector2D(x, y)
            
            x = self.x / other
            y = self.y / other
            return Vector2D(x, y)
        except ZeroDivisionError:
            return Vector2D()
    
    def __itruediv__(self, other):
        try:
            if type(other) == Vector2D:
                self.x /= other.x
                self.y /= other.y
                return self
            
            self.x /= other
            self.y /= other
            return self
        except ZeroDivisionError:
            return Vector2D()

    def __iter__(self):
        return iter((self.x, self.y))
