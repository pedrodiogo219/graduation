import matplotlib.pyplot
import math

def f(x, y):
  return y*y + 1;

def sol(x):
    return math.tan(x)

def main():

    a, b = 0, 1
    h = 0.2
    y0 = 0

    x, y, s = euler(a, b, h, y0, f, sol)
    plota(x, y, s)

    h = 0.02
    x, y, s = euler(a, b, h, y0, f, sol)
    plota(x, y, s)
    matplotlib.pyplot.show()


def euler(a, b, h, y0, f, sol):
    y = []
    x = []
    s = []

    x.append(a)
    y.append(y0)
    s.append(sol(a))

    yn = y0
    xn = a
    while xn <= b :
        yn1 = yn + h*( f(xn, yn) )
        xn1 = xn + h

        s.append(sol(xn1))
        x.append(xn1)
        y.append(yn1)

        xn = xn1
        yn = yn1

    return (x, y, s)


def plota(x, y, sol):
    matplotlib.pyplot.plot(x, sol, "ro")
    matplotlib.pyplot.plot(x, y, "o")




main()
