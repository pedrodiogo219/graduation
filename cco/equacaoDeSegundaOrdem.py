from matplotlib.pyplot import plot
from matplotlib.pyplot import show


def f(tn, yn, zn):
  return zn

def g(tn, yn, zn):
    A = 2
    m = 1
    n = 0.8

    if zn > 0:
        return (-A - n**2 * yn)/m
    else:
        return (A - n**2 * yn)/m




def main():


    z = 0
    y = 3
    t = 0

    Y = y
    Z = z

    h = 0.1

    yn = []
    tn = []
    zn = []
    Yl = []
    Zl = []

    while t <= 5:
        tn.append(t)
        yn.append(y)
        zn.append(z)
        Yl.append(Y)
        Zl.append(Z)

        kf1 = f(t, y, z)
        kg1 = g(t, y, z)

        kf2 = f(t + h/2, y+((h/2)*kf1), z+((h/2)*kg1))
        kg2 = g(t + h/2, y+((h/2)*kf1), z+((h/2)*kg1))


        Yn = Y + h*f(t, Y, Z)
        Zn = Z + h*g(t, Y, Z)
        Y = Yn
        Z = Zn


        t+=h
        y = y + h*kf2
        z = z + h*kg2


    print("yn: ", end="")
    print(yn)
    print("zn: ", end="")
    print(zn)

    plotaPraMin(tn, yn, zn, Yl, Zl)


def plotaPraMin(xn, yn, zn, Yn, Zn):
    plot(xn, yn, 'R')
    plot(xn, zn, 'G')
    plot(xn, Yn, 'Y')
    plot(xn, Zn, 'B')
    show()









main()
