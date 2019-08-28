import math
import matplotlib.pyplot

def f(x, y):
    return -y + x + 2

def f1(x, y):
    return y - x - 1

def f2(x, y):
    return -y + x + 1

def sol(x):
    return (math.e**(-x)) + x + 1


def taylor(a, b, h, y0):
    x = []
    y = []
    s = []

    x.append(a)
    y.append(y0)
    s.append(sol(a))
    xn = a
    yn = y0

    while xn <= b:
        yn = yn + h*f(xn, yn) + (h*h)/2.0 * f1(xn, yn) + (h*h*h)/6.0 * f2(xn, yn)
        xn += h

        x.append(xn)
        y.append(yn)
        s.append(sol(xn))


    return (x, y, s)

def plota(x, y, mx, ms):
    matplotlib.pyplot.plot(x, y, "o")
    matplotlib.pyplot.plot(mx, ms, "r")
    matplotlib.pyplot.show()



def main():
    a, b = 0, 0.3
    h = 0.01
    y0 = 2

    x, y, s = taylor(a, b, h, y0)
    print(x)
    print(y)
    print(s)

    meus = []
    meux = []

    xn = 0
    while xn <= 0.3:
        meux.append(xn)
        meus.append(sol(xn))
        xn+=0.0001

    plota(x, y, meux, meus)



main()
