from silverelephant import *
import numpy as np

def graph(f, X, offset=Vector2(0,0), scale=Vector2(1, 1)):
    beginShape()
    for x in X:
        vertex(x*scale.x+offset.x, f(x)*scale.y+offset.y)
    endShape(connect=False)

def coordinateSystem(offset, scale):
    stroke([50, 50, 50, 255])
    noFill()
    line(0, 0, 0, CANVAS.height)
    line(0, 0, CANVAS.width, 0)
    line(0, 0, 0, -CANVAS.height)
    line(0, 0, -CANVAS.width, 0)


setup(1000, 1000)
while not closed():
    beginFrame()
    background([225, 225, 225, 255])
    noFill()
    stroke([50, 50, 50, 255])
    strokeWeight(2)
    coordinateSystem(Vector2(0, -CANVAS.height), Vector2(1, 1))
    graph(lambda x : math.e**x, np.arange(-10, 10, 0.1), offset=Vector2(0, 0), scale=Vector2(1000, 100))


    endFrame()

end()