from pyglet.shapes import Circle, Arc
from . import Vector2D, circle_parametric

class Point:
    def __init__(self, x=0, y=0, radius=5, color=(255, 255, 255), batch=None):
        self._pos = Vector2D(x, y)
        self.velocity = Vector2D()
        self.acceleration = Vector2D()
        self.direction = 0
        self.shape = Circle(x, y, radius, color=color, batch=batch)

    def update(self, dt):
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        self.shape.position = self.x, self.y

    def draw(self):
        self.shape.draw()

    @property
    def position(self):
        return self._pos
    
    @position.setter
    def position(self, value):
        self._pos.x, self._pos.y = value
        self.shape.position = value
    
    @property
    def x(self):
        return self._pos.x
    
    @x.setter
    def x(self, value):
        self._pos.x = value
        self.shape.x = value
    
    @property
    def y(self):
        return self._pos.y
    
    @y.setter
    def y(self, value):
        self._pos.y = value
        self.shape.y = value

class Part(Point):
    def __init__(self, x=0, y=0, radius=5, size=50, color=(255, 255, 255), batch=None):
        super().__init__(x, y, radius, color, batch)

        self._batch = batch
        self.size = size
        self.outer = Arc(x, y, size, color=color + (100,), batch=batch)

        self.outline = []
        self.solve_outline_points()
    
    def solve_outline_points(self):
        self.outline = []
        dir = self.direction

        x, y = circle_parametric(self.size, self.direction + 90)
        x += self.x
        y += self.y
        self.outline.append(Point(x, y, batch=self._batch))

        x, y = circle_parametric(self.size, self.direction - 90)
        x += self.x
        y += self.y
        self.outline.append(Point(x, y, batch=self._batch))

    def update(self, dt):
        super().update(dt)
        self.outer.position = (self.x, self.y)
        self.solve_outline_points()
    
    def draw(self):
        super().draw()
        self.outer.draw()
        for point in self.outline:
            point.draw()