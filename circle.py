# babavoss.pythonanywhere.com/python/bresenham-line-drawing-algorithm-implemented-in-py
import math
import random

from OpenGL.GL import *
from OpenGL.GLUT import *

from linealgorithm import generatePixel, generatePixelForCircle

width, height = 500, 800
handler_x = 0

handler_x_left = 150
handler_x_right = 150
bullet_y = 0
handler_upper_range = 15
initial_circle_value_x = random.randint(0, 500)
initial_circle_value_y = 740
targetBulletSize = 15

initial_bullet_x = 0
initial_bullet_y = 0
bullet_speed = 0
bullet_velocity_y = 0
x1 = 0
y1 = 0
handler_center_x = 0
handler_center_y = 0
is_up_key_pressed = False
is_bullet_exists = True
is_bullet_clashed = False


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
    global handler_center_x
    global handler_center_y
    glColor3f(0.0, 1.0, 0.0)
    handler_center_x, handler_center_y = 160 + x, handler_upper_range
    handler_x_left = x1
    handler_x_right = x1 + 20
    x_list, y_list = generatePixelForCircle(10, handler_center_x, handler_center_y)
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
    global initial_circle_value_x
    global initial_circle_value_y
    global bullet_y
    global targetBulletSize
    global is_bullet_clashed
    # drawing the cross
    x1, y1 = initial_circle_value_x, initial_circle_value_y + y
    x_list, y_list = generatePixelForCircle(targetBulletSize, x1, y1)
    drawDots(x_list, y_list)
    if y1 < 0:
        initial_circle_value_x = random.randint(0, 500)
        bullet_y = 0
        is_bullet_clashed = False


def display():
    global is_up_key_pressed
    global is_bullet_clashed
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    interate()
    drawBullet(bullet_y)
    drawCross()
    drawHandler(handler_x)
    drawPause()
    drawArrowSign()
    if is_up_key_pressed and not is_bullet_clashed:
        fireBullet()
        glutPostRedisplay()
    glutSwapBuffers()


def handle_keys(key, x, y):
    global handler_x
    global handler_x_left
    global handler_x_right
    global is_up_key_pressed
    global initial_bullet_x
    global handler_center_x
    global is_bullet_exists
    global is_bullet_clashed
    if key == GLUT_KEY_LEFT and handler_x_left >= 0:
        handler_x -= 5
    elif key == GLUT_KEY_RIGHT and handler_x_right < 500:
        handler_x += 5
    elif key == GLUT_KEY_UP:
        is_up_key_pressed = True
        if is_bullet_exists:
            initial_bullet_x = handler_center_x
            is_bullet_exists = False
            is_bullet_clashed = False
    glutPostRedisplay()


def fireBullet():
    global handler_center_y

    global initial_bullet_x
    global initial_bullet_y
    global bullet_speed
    global is_up_key_pressed
    global is_bullet_exists
    global bullet_y
    global is_bullet_clashed
    global initial_circle_value_x
    initial_bullet_y = handler_center_y + bullet_speed
    x_list, y_list = generatePixelForCircle(targetBulletSize, initial_bullet_x, initial_bullet_y)
    drawDots(x_list, y_list)
    if (circles_touch_or_overlap(initial_bullet_x, initial_bullet_y, targetBulletSize,
                                 initial_circle_value_x, initial_circle_value_y + bullet_y, targetBulletSize)):
        print("match")
        is_bullet_clashed = True
        is_up_key_pressed = False
        is_bullet_exists = True
        bullet_speed = 0
        initial_circle_value_x = random.randint(0, 500)
        bullet_y = 0
        is_bullet_clashed = False
    if initial_bullet_y > 740:
        bullet_speed = 0
        is_up_key_pressed = False
        is_bullet_exists = True


def circles_touch_or_overlap(x1, y1, r1, x2, y2, r2):
    # Calculate the distance between the centers of the circles
    distance_centers = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Check if the distance between the centers is less than or equal to the sum of the radii
    if distance_centers <= r1 + r2:
        # Circles touch or overlap
        return True
    else:
        # Circles do not touch
        return False


def animateTarget(value):
    global bullet_y
    global bullet_speed
    bullet_y -= 5
    if is_up_key_pressed:
        bullet_speed += 25
    glutPostRedisplay()
    glutTimerFunc(100, animateTarget, 0)


if __name__ == "__main__":
    glutInit()
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("DDA Line")
    glutDisplayFunc(display)
    glutSpecialFunc(handle_keys)
    glutTimerFunc(0, animateTarget, 0)
    glutMainLoop()
