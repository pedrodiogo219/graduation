import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import pywavefront
from pywavefront import visualization
import math

obj = []

CameraPosition = [0.0,0.0,0.0]
CameraTarget=[-0.728225,0.199367,0.655697]
up_axis = [0.0,1.0,0.0]
lastX = 0.0
lastY = 0.0
firstMouse = True
Velocidade_camera = 0.5
sensibilidade = 0.2

pitch = -16.0
yaw = -182.5

def cross(x,y):
    aux =  [ x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[1]]
    return  aux

def display():
    global obj

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(CameraPosition[0],CameraPosition[1],CameraPosition[2],
              CameraPosition[0]+CameraTarget[0],CameraPosition[1]+CameraTarget[1],CameraPosition[2]+CameraTarget[2],
              up_axis[0],up_axis[1],up_axis[2])
    visualization.draw(obj)
    glutSwapBuffers()
    return



def mouseMove(x, y):

    print(CameraTarget[0],' - ',CameraTarget[1],' - ',CameraTarget[2],' - ')
    global lastX
    global lastY
    global sensibilidade
    global pitch
    global yaw
    global firstMouse
    print('pitch - ',pitch)
    print('yaw - ',yaw)

    if firstMouse:
      lastX = x
      lasty = y
      firstMouse = False

    dx = x - lastX
    dy = lastY-y
    lastX = x
    lastY = y

    dx *= sensibilidade
    dy *= sensibilidade

    yaw += dx
    pitch += dy


    if pitch > 89.0:
      pitch = 89.0
    elif pitch < -89.0:
      pitch = -89.0

                    #calculando os radianos do vertical e do horizontal
    rpitch = (math.pi * pitch)/180
    ryaw = (math.pi*yaw)/180

    CameraTarget[0] = math.cos(ryaw)* math.cos(rpitch)
    CameraTarget[1] = math.sin(rpitch)
    CameraTarget[2] = math.cos(rpitch)*math.sin(ryaw)

                                #normalização
    n  = math.sqrt(CameraTarget[0]*CameraTarget[0] + CameraTarget[1]*CameraTarget[1]+CameraTarget[2]*CameraTarget[2])
    CameraTarget[0]= CameraTarget[0]/n
    CameraTarget[1]= CameraTarget[1]/n
    CameraTarget[2]= CameraTarget[2]/n

    glutPostRedisplay()


def keyboard(key, xx, yy):
  atY = CameraPosition[1]
    #ir para a esquerda
  if ord(key) == ord('a'):
    aux = cross(CameraTarget,up_axis)
    n  = math.sqrt(aux[0]*aux[0] + aux[1]*aux[1]+aux[2]*aux[2])
    aux[0]= aux[0]/n
    aux[1]= aux[1]/n
    aux[2]= aux[2]/n
    CameraPosition[0]-= aux[0]*Velocidade_camera
    CameraPosition[1]-= aux[1]*Velocidade_camera
    CameraPosition[2]-= aux[2]*Velocidade_camera
    CameraPosition[1] = atY
    glutPostRedisplay()
    #ir para direita
  if ord(key) == ord('d'):
    aux = cross(CameraTarget,up_axis)
    n  = math.sqrt(aux[0]*aux[0] + aux[1]*aux[1]+aux[2]*aux[2])
    aux[0]= aux[0]/n
    aux[1]= aux[1]/n
    aux[2]= aux[2]/n
    CameraPosition[0]+= aux[0]*Velocidade_camera
    CameraPosition[1]+= aux[1]*Velocidade_camera
    CameraPosition[2]+= aux[2]*Velocidade_camera
    CameraPosition[1] = atY
    glutPostRedisplay()

    #ir para frente
  if ord(key) == ord('w'):
    CameraPosition[0]+= CameraTarget[0]*Velocidade_camera
    CameraPosition[1]+= CameraTarget[1]*Velocidade_camera
    CameraPosition[2]+= CameraTarget[2]*Velocidade_camera
    CameraPosition[1] = atY
    glutPostRedisplay()
    #ir para trás
  if ord(key) == ord('s'):
    CameraPosition[0]-= CameraTarget[0]*Velocidade_camera
    CameraPosition[1]-= CameraTarget[1]*Velocidade_camera
    CameraPosition[2]-= CameraTarget[2]*Velocidade_camera
    CameraPosition[1] = atY
    glutPostRedisplay()

    #aumenta a "altura" da camera
  if ord(key) == 56:
    CameraPosition[1]+=Velocidade_camera
    glutPostRedisplay()
    #diminui a "altura" da camera
  if ord(key) == 50:
    CameraPosition[1]-=Velocidade_camera
    glutPostRedisplay()



glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(900,800)
glutCreateWindow("Bar que nao deu certo :( - RCL")
glutDisplayFunc(display)
glClearColor(0.1,0.1,0.1,0.1)

glShadeModel(GL_SMOOTH)
glEnable(GL_CULL_FACE)
glEnable(GL_DEPTH_TEST)

lightZeroPosition = [0.0,30.0,-30.0,20.0]
lightZeroColor = [1,0.8,0.4,1]
lightSpecular = [0.5,0.5,0.5,0.5]
lightAmbiente = [0.0,0.0,0.0,1]

glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
glLightfv(GL_LIGHT0, GL_DIFFUSE, lightZeroColor)
glLightfv(GL_LIGHT0, GL_SPECULAR, lightSpecular)
glLightfv(GL_LIGHT0, GL_AMBIENT, lightAmbiente)
glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.4)
glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.07)
glEnable(GL_LIGHT0)
glEnable(GL_LIGHTING)

glutDisplayFunc(display)
glMatrixMode(GL_PROJECTION)
gluPerspective(30.,1.,0.1,80.)
glMatrixMode(GL_MODELVIEW)
gluLookAt(CameraPosition[0],CameraPosition[1],CameraPosition[2],
              CameraTarget[0]+CameraPosition[0],CameraTarget[1]+CameraPosition[1],CameraTarget[2]+CameraPosition[2],
              up_axis[0],up_axis[1],up_axis[2])


obj = pywavefront.Wavefront('Car.obj',create_materials=True,collect_faces=True)
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutPassiveMotionFunc(mouseMove)

glutMainLoop()
