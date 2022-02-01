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
        self.strokeWeight = 2

class Meshes:
    def __init__(self):
        self.mainCol = [1, 1, 1, 1]
        self.fill = True
        self.shape = False
        self.curVertices = []

CANVAS = Window()
STROKE = Stroke()
MESHES = Meshes()

def setup(width, height):
    glfw.init()
    window = glfw.create_window(width, height,'SilverElephant', None, None)
    CANVAS.width = width
    CANVAS.height = height
    CANVAS.W = window
    glfw.set_window_pos(window, 400, 200)
    glfw.make_context_current(window)

def background(color):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(color[0]/255,color[1]/255,color[2]/255,color[3]/255)

def beginFrame():
    glfw.poll_events()

def endFrame():
    glfw.swap_buffers(CANVAS.W)

def closed():
    return glfw.window_should_close(CANVAS.W) 

def line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glColor(MESHES.mainCol)
    glVertex2f(x1/CANVAS.width, y1/CANVAS.width)
    glVertex2f(x2/CANVAS.width, y2/CANVAS.width)
    glEnd()

def rect(x, y, width, height):
    p1 = [x, y]
    p2 = [x + width, y]
    p3 = [x + width, y + height]
    p4 = [x, y + height]
    if MESHES.fill:
        glBegin(GL_QUADS)
        glColor(MESHES.mainCol)
        glVertex2f(p1[0]/CANVAS.width, p1[1]/CANVAS.width)
        glVertex2f(p2[0]/CANVAS.width, p2[1]/CANVAS.width)
        glVertex2f(p3[0]/CANVAS.width, p3[1]/CANVAS.width)
        glVertex2f(p4[0]/CANVAS.width, p4[1]/CANVAS.width)
        glEnd()
    if STROKE.stroke:
        glLineWidth(STROKE.strokeWeight) 
        glBegin(GL_LINE_LOOP)
        glColor(STROKE.strokeCol)
        glVertex2f(p1[0]/CANVAS.width, p1[1]/CANVAS.width)
        glVertex2f(p2[0]/CANVAS.width, p2[1]/CANVAS.width)
        glVertex2f(p3[0]/CANVAS.width, p3[1]/CANVAS.width)
        glVertex2f(p4[0]/CANVAS.width, p4[1]/CANVAS.width)
        glEnd()

def circle(x, y, radius):
    if MESHES.fill:
        glBegin(GL_POLYGON)
        glColor(MESHES.mainCol)
        for theta in range(360):
            X = math.cos((theta*(math.pi/180))) * radius + x
            Y = math.sin((theta*(math.pi/180))) * radius + y
            glVertex2f(X/CANVAS.width, Y/CANVAS.height)
        glEnd()
    if STROKE.stroke:
        glLineWidth(STROKE.strokeWeight) 
        glBegin(GL_LINE_LOOP)
        glColor(STROKE.strokeCol)
        for theta in range(360):
            X = math.cos((theta*(math.pi/180))) * radius + x
            Y = math.sin((theta*(math.pi/180))) * radius + y
            glVertex2f(X/CANVAS.width, Y/CANVAS.height)
        glEnd()
    
def point(x, y, size):
    circle(x, y, size)

def beginShape(): 
  MESHES.shape = True

def endShape():
  MESHES.shape = False
  if MESHES.fill:
    glBegin(GL_POLYGON)
    glColor(MESHES.mainCol)    
    for vertex in MESHES.curVertices:
      glVertex2f(vertex[0], vertex[1])
    glEnd()
  if STROKE.stroke:
    glLineWidth(STROKE.strokeWeight)
    glBegin(GL_LINE_LOOP)
    glColor(STROKE.strokeCol)
    for vertex in MESHES.curVertices:
      glVertex2f(vertex[0], vertex[1])
    glEnd()
    
      
  MESHES.curVertices = []

def vertex(x, y):
  if MESHES.shape:
    MESHES.curVertices.append([x/CANVAS.width, y/CANVAS.height])
  else:
    print('Cannot add a vertex without beginShape()')

def fill(col):
    """ Set the color of filled objects """
    MESHES.mainCol = [col[0]/255, col[1]/255, col[2]/255, col[3]/255]
    MESHES.fill = True

def noFill():
    """ Turn filling off """
    MESHES.fill = False

def noStroke():
    """ Turn off the stroke  """
    STROKE.stroke = False

def stroke(col):
    """ Set the stroke color """
    STROKE.stroke = True
    STROKE.strokeCol = [col[0]/255, col[1]/255, col[2]/255, col[3]/255]

def strokeWeight(weight):
    STROKE.strokeWeight = weight

def end():
    glfw.terminate()