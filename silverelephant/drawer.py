from .core import *

class Window:
    def __init__(self):
        self.width = 0
        self.height = 0
        self.W = None

class Stroke:
    def __init__(self):
        self.strokeCol = [1, 1, 1, 1]
        self.stroke = False

class Meshes:
    def __init__(self):
        self.mainCol = [1, 1, 1, 1]
        self.fill = True

CANVAS = Window()
STROKE = Stroke()
MESHES = Meshes()

def setup(width, height):
    glfw.init()
    window = glfw.create_window(width, height,'SilverElephant', None, None)
    CANVAS.WIDTH = width
    CANVAS.HEIGHT = height
    CANVAS.W = window
    glfw.set_window_pos(window, 400, 200)
    glfw.make_context_current(window)
    return window

def background(color):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(color[0],color[1],color[2],color[3])

def beginFrame():
    glfw.poll_events()

def endFrame():
    glfw.swap_buffers(CANVAS.W)

def closed():
    return glfw.window_should_close(CANVAS.W) 

def line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def rect(x, y, width, height):
    p1 = [x, y]
    p2 = [x + width, y]
    p3 = [x + width, y + height]
    p4 = [x, y + height]
    glBegin(GL_QUADS if MESHES.fill else GL_LINES_LOOP)
    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p2[1])
    glVertex2f(p3[0], p3[1])
    glVertex2f(p4[0], p4[1])
    glEnd()
    if STROKE.stroke:
        glBegin(GL_LINE_LOOP)
        glColor(STROKE.strokeCol)
        glVertex2f(p1[0], p1[1])
        glVertex2f(p2[0], p2[1])
        glVertex2f(p3[0], p3[1])
        glVertex2f(p4[0], p4[1])
        glEnd()
        glColor(MESHES.mainCol)

def color(col):
    """ Set the color of filled objects """
    glColor(col)
    MESHES.mainCol = col

def setFill(fill):
    """ Set the fill boolean """
    MESHES.fill = fill

def noStroke():
    """ Turn off the stroke  """
    STROKE.stroke = False

def stroke(col):
    """ Set the stroke color """
    STROKE.stroke = True
    STROKE.strokeCol = col

def end():
    glfw.terminate()
