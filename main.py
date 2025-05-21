from random import randint
import pyglet
from pyglet.window import key
from engine import Part, DistanceConstraint, circle_parametric

window = pyglet.window.Window()
window.set_size(1024, 768)
window.set_caption('Physics Engine')

point_batch = pyglet.graphics.Batch()
constraint_batch = pyglet.graphics.Batch()

def create_body(sizes=[50]):
    body = []
    for size in sizes:
        x = randint(0, 1024)
        y = randint(0, 768)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        body.append(Part(x, y, size=size, color=color, batch=point_batch))

    constraints = []
    for i in range(len(sizes)-1):
        constraints.append(DistanceConstraint(body[i], body[i+1], length=50, color=(200, 200,200), batch=constraint_batch))
    
    return body, constraints

body, constraints = create_body([45, 50, 40, 30, 15])

movements = {'up': False, 'down': False, 'left': False, 'right': False}

@window.event
def on_key_press(symbol, modifier):
    if symbol == key.W:
        movements['up'] = True
    if symbol == key.S:
        movements['down'] = True
    if symbol == key.A:
        movements['left'] = True
    if symbol == key.D:
        movements['right'] = True

@window.event
def on_key_release(symbol, modifier):
    if symbol == key.W:
        movements['up'] = False
    if symbol == key.S:
        movements['down'] = False
    if symbol == key.A:
        movements['left'] = False
    if symbol == key.D:
        movements['right'] = False

@window.event
def on_draw():
    window.clear()
    constraint_batch.draw()
    point_batch.draw()

def body_movement(dt, speed, target_friction):
    control_x = movements['right'] - movements['left']
    control_y = movements['up'] - movements['down']

    body[0].velocity.x += control_x * dt * speed
    body[0].velocity.y += control_y * dt * speed

    friction = 1 - dt * target_friction / (1 - dt)

    body[0].velocity.x *= friction
    body[0].velocity.y *= friction

def update(dt):
    body_movement(dt, speed=100, target_friction = 0.99)

    for parts in body:
        parts.update(dt)
    for constraint in constraints:
        constraint.update(dt)

initialized = True
pyglet.clock.schedule_interval(update, 1/60)
pyglet.app.run()