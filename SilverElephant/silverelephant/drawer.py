from .core import *

def setup(width, height):
    glfw.init()
    window = glfw.create_window(width, height,'SilverElephant', None, None)
    glfw.set_window_pos(window, 400, 200)
    glfw.make_context_current(window)
    return window

def background(color):
    glClear(GL_COLOR_BUFFER_BIT)
    glClearColor(color[0],color[1],color[2],color[3])

def beginFrame():
    glfw.poll_events()

def endFrame(win):
    glfw.swap_buffers(win)

def closed(window):
    return glfw.window_should_close(window) 

def line(p1, p2, col):
    glBegin(GL_LINES)
    glColor(col)
    glVertex2f(p1[0], p1[1])
    glVertex2f(p2[0], p2[1])
    glEnd()

def end():
    glfw.terminate()
