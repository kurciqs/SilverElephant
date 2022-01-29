from silverelephant import *

WIN = setup(800, 600)
i = 0
while not closed():
    beginFrame()
    background([0,  0, 0, 1])
    color([0, 0, 0, 1])
    stroke([1, 1, 1, 1])
    rect(-0.5, -0.5, i, i)
    i += 0.001
    endFrame()

end()
