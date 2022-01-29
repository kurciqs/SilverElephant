from silverelephant import *

WIN = setup(800, 600)
i = 0
while not closed(WIN):
    beginFrame()
    background([0,  0, 0.2, 1])
    line([i, 0], [0.5, 0.5], [1, 1, 1, 1])
    i += 0.001
    endFrame(WIN)

end()
