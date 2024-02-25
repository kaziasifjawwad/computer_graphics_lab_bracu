from OpenGL.GL import *
from OpenGL.GLUT import *

# Window dimensions
from linealgorithm import generatePixel

width, height = 500, 800


def interate():
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, width, 0.0, height, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def drawLineDDA(x_list, y_list):
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
    drawLineDDA(x_list, y_list)
    x1, y1 = 20, 760
    x2, y2 = 50, 740
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawLineDDA(x_list, y_list)
    x1, y1 = 20, 760
    x2, y2 = 70, 760
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawLineDDA(x_list, y_list)


def drawPause():
    glColor3f(0.0, 1.0, 0.0)
    # Start pause
    x1, y1 = 230, 780
    x2, y2 = 230, 740
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawLineDDA(x_list, y_list)
    x1, y1 = 240, 780
    x2, y2 = 240, 740
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawLineDDA(x_list, y_list)

def drawHandler():
    glColor3f(0.0, 1.0, 0.0)
    x1, y1 = 160, 15
    x2, y2 = 290, 15
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawLineDDA(x_list, y_list)
    x1, y1 = 160, 25
    x2, y2 = 290, 25
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawLineDDA(x_list, y_list)


def drawCross():
    # drawing the cross
    x1, y1 = 440, 780
    x2, y2 = 480, 740
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawLineDDA(x_list, y_list)
    x1, y1 = 480, 780
    x2, y2 = 440, 740
    x_list, y_list = generatePixel(x1, y1, x2, y2)
    drawLineDDA(x_list, y_list)




def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    interate()

    drawCross()
    drawHandler()
    drawPause()
    drawArrowSign()
    glutSwapBuffers()


if __name__ == "__main__":
    glutInit()  # Initialize GLUT
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)  # Add GLUT_DOUBLE for double buffering
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("DDA Line")

    # Register display function
    glutDisplayFunc(display)

    glutMainLoop()
