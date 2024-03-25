#babavoss.pythonanywhere.com/python/bresenham-line-drawing-algorithm-implemented-in-py

import random

from OpenGL.GL import *
from OpenGL.GLUT import *

from linealgorithm import generatePixel, generatePixelForCircle

width, height = 500, 800
handler_x = 0
handler_y = 0
handler_x_left = 150
handler_x_right = 150
bullet_y = 0
handler_upper_range = 15
initial_diamond_value_x = random.randint(0, 500)
initial_diamond_value_y = 740
targetBulletSize = 15

def interate():
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def drawDots(x_list, y_list):
    glBegin(GL_POINTS)
    for i in range(len(x_list)):
        glVertex2f(x_list[i], y_list[i])
    glEnd()


def drawArrowSign():
    glColor3f(0.0, 1.0, 0.0)
    # Arrow sign
    x1, y1 = 50, 780
    x2, y2 = 20, 760
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawDots(x_list, y_list)
    x1, y1 = 20, 760
    x2, y2 = 50, 740
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawDots(x_list, y_list)
    x1, y1 = 20, 760
    x2, y2 = 70, 760
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawDots(x_list, y_list)


def drawPause():
    glColor3f(0.0, 1.0, 0.0)
    # Start pause
    x1, y1 = 230, 780
    x2, y2 = 230, 740
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawDots(x_list, y_list)
    x1, y1 = 240, 780
    x2, y2 = 240, 740
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawDots(x_list, y_list)


def drawHandler(x):
    global handler_upper_range
    global handler_x_left
    global handler_x_right
    glColor3f(0.0, 1.0, 0.0)
    x1, y1 = 160 + x, handler_upper_range
    handler_x_left = x1
    handler_x_right = x1+20
    x_list, y_list = generatePixelForCircle(10,x1, y1)
    drawDots(x_list, y_list)


def drawCross():
    # drawing the cross
    x1, y1 = 440, 780
    x2, y2 = 480, 740
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawDots(x_list, y_list)
    x1, y1 = 480, 780
    x2, y2 = 440, 740
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawDots(x_list, y_list)


def drawBullet(y):
    global handler_upper_range
    global handler_x_left
    global handler_x_right
    global initial_diamond_value_x
    global initial_diamond_value_y
    global bullet_y
    global targetBulletSize
    # drawing the cross
    x1, y1 = initial_diamond_value_x, initial_diamond_value_y + y
    x_list, y_list = generatePixelForCircle(targetBulletSize,x1, y1)
    drawDots(x_list, y_list)
    print(y1)
    if y1<0:
        initial_diamond_value_x = random.randint(0, 500)
        bullet_y = 0


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    interate()
    drawBullet(bullet_y)
    drawCross()
    drawHandler(handler_x)
    drawPause()
    drawArrowSign()
    glutSwapBuffers()


def handle_keys(key, x, y):
    global handler_x
    global handler_x_left
    global handler_x_right
    if key == GLUT_KEY_LEFT and handler_x_left >= 0:
        handler_x -= 5
    elif key == GLUT_KEY_RIGHT and handler_x_right < 500:
        handler_x += 5
    glutPostRedisplay()


def animateBullet(value):
    global bullet_y
    bullet_y -= 5
    glutPostRedisplay()
    glutTimerFunc(100, animateBullet, 0)  # Recursive call to keep animating the bullet


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("DDA Line")
    glutDisplayFunc(display)
    glutSpecialFunc(handle_keys)
    glutTimerFunc(0, animateBullet, 0)  # Start bullet animation
    glutMainLoop()
