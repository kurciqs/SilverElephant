from silverelephant import *


class Ball:
    def __init__(self, mass) -> None:
        self.pos = Vector2(0, 0)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)
        self.mass = mass
        self.radius = math.sqrt(mass) * 50

    def show(self):
        stroke([255, 0, 0, 255])
        fill([0, 0, 0, 255])
        circle(self.pos.x, self.pos.y, self.radius)

    def applyForce(self, force):
        f = copy.deepcopy(force)
        f.div(self.mass)
        self.acc.add(f)

    def update(self):
        self.vel.add(self.acc)
        self.pos.add(self.vel)
        self.acc.set(0, 0)
        
    def edges(self):
        if self.pos.y <= -CANVAS.height + self.radius:
            self.pos.y = -CANVAS.height + self.radius
            self.vel.y *= (-1)

        if self.pos.y >= CANVAS.height - self.radius:
            self.pos.y = CANVAS.height - self.radius
            self.vel.y *= (-1)

        if self.pos.x <= -CANVAS.width + self.radius:
            self.pos.x = -CANVAS.width + self.radius
            self.vel.x *= (-1)
            
        if self.pos.x >= CANVAS.width - self.radius:
            self.pos.x = CANVAS.width - self.radius
            self.vel.x *= (-1)

    