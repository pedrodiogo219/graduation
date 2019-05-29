from numpy import *
import math
import matplotlib.pyplot as plt
"""
x = []
y1 = []
y2 = []
for n in range(0, 5000, 100):
  x.append(n)
  y2.append( n**2 )
  y1.append( n**2.7 )



plt.plot(x, y1)
plt.plot(x, y2)
plt.savefig('teoria.png')
"""

t = linspace([1,2,3],10)
a = (lambda x: x**2)(t)
b = (lambda x: x**2.7)(t)
c = (lambda x: x**3)(t)
d = (lambda x: x*log2(x))(t)

plt.plot(t, a, 'r')
plt.plot(t, b, 'g')
plt.plot(t, c, 'b')
plt.plot(t, d, 'y')
plt.savefig('comparacao_complexidades.png')
