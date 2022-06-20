import matplotlib.pyplot as plt
import math
import numpy as np

a = int(input('Input a: '))
b = int(input('Input b: '))
c = int(input('Input c: '))

# calculate delta and zero points
d = b**2 - 4*a*c
if d > 0:
    x1 = (-b + math.sqrt(d))/(2*a)
    x2 = (-b - math.sqrt(d))/(2*a)
if d == 0:
    v = -b/(2*a)
else:
    pass

# calculate parabola extreme coordinates
p = -b/(2*a)
q = -d/(4*a)
extreme = [p,q]

# define parabola function
def parabola(x,a,b,c):
    y = a*x**2 + b*x + c
    return y

# plot function
x = np.linspace(int(p)-5,int(p)+5,100)
y = parabola(x,a,b,c)
plt.plot(x,y)
plt.axhline(y=0, color='black', linestyle='-')
plt.axvline(x=0, color='black', linestyle='-')
plt.text(p-0.5, q-3, '[' + str(round(p,2)) +',' + str(round(q,2)) + ']',color='orange', fontsize=9)
plt.plot(p, q, marker="o")

if d > 0:
    plt.plot(x1, 0, marker="o", color='green')
    plt.text(x1 - 0.5, 2, '[' + str(round(x1,2)) + ']', color='green', fontsize=9)
    plt.plot(x2, 0, marker="o", color='green')
    plt.text(x2 - 0.5, 2, '[' + str(round(x2,2)) + ']', color='green', fontsize=9)

if d == 0:
    plt.plot(v, 0, marker="o", color='green')
    plt.text(v - 0.5, 2, '[' + str(round(v,2)) + ']', color='green', fontsize=9)

plt.show()
