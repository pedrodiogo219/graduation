import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pywavefront
from pywavefront import visualization

name = 'example_output'
obj = []
mouseButtonPressed = None
MousePos = [0,0]
teste2 =0

def keyboard(key, x, y):

  if ord(key) == 49:#'1'
    glLoadIdentity();
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)

    glutPostRedisplay()
  if ord(key) == 50:#'2'
    glLoadIdentity();1
    gluLookAt(0,0,20,
              0,0,0,
              0,1,0)
    glutPostRedisplay()
  if ord(key) == 51:#'3'
    glRotatef(-15.0,1.0,0.0,0.0)
    glutPostRedisplay()
  if ord(key) == 52:#'4'
    glRotatef(-15.0,0.0,1.0,0.0)
    glutPostRedisplay()
  if ord(key) == 53:#'5'
    glRotatef(-15.0,0.0,0.0,1.0)
    glutPostRedisplay()
  if ord(key) == 54:#'6'
    glTranslatef(0.0,0.0,0.1)
    glutPostRedisplay()
  if ord(key) == 55:#'7'
    glTranslatef(0.0,0.0,-0.1)
    glutPostRedisplay()

  if ord(key) == ord('a'):
    glTranslatef(0.1,0.0,0.0)
    glutPostRedisplay()

  if ord(key) == ord('d'):
    glTranslatef(-0.1,0.0,0.0)
    glutPostRedisplay()

  if ord(key) == ord('e'):
    glTranslatef(0.0,0.1,0.0)
    glutPostRedisplay()

  if ord(key) == ord('q'):
    glTranslatef(0.0,-0.1,0.0)
    glutPostRedisplay()

  if ord(key) == ord('s'):
    glTranslatef(0.0,0.0,0.1)
    glutPostRedisplay()

  if ord(key) == ord('w'):
    glTranslatef(0.0,0.0,-0.1)
    glutPostRedisplay()
  if ord(key) == ord('p'):
    lightZeroPosition = [20.,2.,-2.,1.]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glutPostRedisplay()
  if ord(key) == ord('o'):
    lightZeroPosition = [-20.,2.,-2.,1.]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glutPostRedisplay()
  if ord(key) == ord('l'):
    lightZeroPosition = [20.,20.,-2.,1.]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glutPostRedisplay()


def GerenciarMouse(button, state, x, y):
    global mouseButtonPressed
    global MousePos

    if(state == GLUT_DOWN):
      mouseButtonPressed = button

    else:
      mouseButtonPressed = None

    MousePos[0], MousePos[1] = x,y

def GerenciarMovimento(x,y):

    deltaX = x - MousePos[0]
    deltaY = y - MousePos[1]

    if(mouseButtonPressed == GLUT_LEFT_BUTTON):
      tX = deltaX * 0.01
      tY = deltaY * 0.01
      glTranslatef(tX,tY,0.0)
      glutPostRedisplay()

    elif(mouseButtonPressed == GLUT_RIGHT_BUTTON):
      rY = deltaX * 1.2
      glRotatef(rY,0,1,0)
      glutPostRedisplay()

      rX = deltaY * 1.2
      glRotatef(rX,1,0,0)
      glutPostRedisplay()

    MousePos[0] = x
    MousePos[1] = y

def main():
    global obj
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow(name)

    glutDisplayFunc(display)
    glutKeyboardFunc(keyboard)
    glutMouseFunc(GerenciarMouse)
    glutMotionFunc(GerenciarMovimento)

    glClearColor(0.3,0.3,0.3,0)


    #glShadeModel(GL_SMOOTH)
    #glEnable(GL_CULL_FACE)
    #glEnable(GL_DEPTH_TEST)
    #glEnable(GL_LIGHTING)
    #lightZeroPosition = [-20.,2.,-2.,1.]
    lightZeroColor = [0.2,0.2,0.2,0.0]
    #lightZeroColor2 = [0.9,0.9,0.9,0.0]
    #glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    #glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor2)
    #glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    #glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    #glEnable(GL_LIGHT0)



    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, lightZeroColor)


    glutDisplayFunc(display)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(30.,1.,0.1,80.)
    glMatrixMode(GL_MODELVIEW)
    gluLookAt(0,0,10,
              0,0,0,
              0,1,0)
    obj = pywavefront.Wavefront('Car.obj')
    #obj = pywavefront.Wavefront('colorsphere.obj')
    #obj = pywavefront.Wavefront('marsexample.obj')

    glutMainLoop()
    return

def display():
    global obj

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE,GL_REPLACE)
    visualization.draw(obj)

    glutSwapBuffers()
    return

if __name__ == '__main__':
    main()
