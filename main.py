from silverelephant import *

WIN = setup(800, 600)
i = 0
while not closed():
    beginFrame()
    background([1, 0, 0, 1])
    stroke([0, 0, 0, 1])
    strokeWeight(1)
    rect(-0.5, -0.5, i, i)
    i += 0.001
    endFrame()

end()
