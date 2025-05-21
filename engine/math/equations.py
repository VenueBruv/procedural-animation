from . import sin, cos, radians

def circle_parametric(radius, angle):
    x = radius * cos(radians(angle))
    y = radius * sin(radians(angle))
    return (x, y)
