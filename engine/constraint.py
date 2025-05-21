from pyglet.shapes import Line, Arc

class Constraint:
    def __init__(self, point_a, point_b, thickness=2, color=(255, 255, 255), batch=None):
        self.point_a = point_a
        self.point_b = point_b

        x1 = point_a.x
        y1 = point_a.y
        x2 = point_b.x
        y2 = point_b.y

        self.line = Line(x1, y1, x2, y2, thickness, color, batch=batch)

    def update(self, dt):
        x1 = self.point_a.x
        y1 = self.point_a.y
        x2 = self.point_b.x
        y2 = self.point_b.y

        self.line.x = x1
        self.line.y = y1
        self.line.x2 = x2
        self.line.y2 = y2

    def draw(self):
        self.line.draw()

class DistanceConstraint(Constraint):
    def __init__(self, point_a, point_b, length=50, thickness=2, color=(255, 255, 255), batch=None):
        super().__init__(point_a, point_b, thickness, color, batch)

        self.length = length

        x = self.point_a.x
        y = self.point_a.y
        # self.range = Arc(x, y, length, color=color + (100,), batch=batch)
    
    def update(self, dt):
        super().update(dt)

        delta = (self.point_b.position - self.point_a.position).normalize()
        self.point_b.direction = delta.direction
        delta *= self.length
        self.point_b.position = self.point_a.position + delta

        # x = self.point_a.x
        # y = self.point_a.y
        # self.range.position = (x, y)
    
    def draw(self):
        super().draw()
        # self.range.draw()