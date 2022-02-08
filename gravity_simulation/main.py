from ball import *
import random

setup(1000, 1000)
BALLS = []
amount = 2

for x in range(amount):
    BALLS.append(Ball(random.randrange(5, 15)))

while not closed():
    beginFrame()
    background([255, 255, 255, 255])


    for BALL in BALLS:

        gravity = Vector2(0, -3)
        gravity.mul(BALL.mass)
        wind = Vector2(1, 0)

        BALL.applyForce(gravity)
        if CANVAS.mouse_L_pressed:
            BALL.applyForce(wind)

        BALL.update()
        BALL.edges()
        BALL.show()


    endFrame()

end()