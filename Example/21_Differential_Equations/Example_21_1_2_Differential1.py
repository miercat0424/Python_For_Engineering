import math as mt
import numpy as np
import matplotlib.pylab as plt

# Parameters
T = 5
a = -1/T

x0  = 1
t   = 0

tstart = 0
tstop  = 25

increment = 1
x = []
x = np.zeros(tstop+1)

t = np.arange(tstart,tstop+1, increment)

# Define the Equation
for k in range(tstop):
    x[k] = mt.exp(a*t[k]) * x0

plt.plot(t,x)
plt.title("Plotting Differntial Equation Solution")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.axis([0,25,0,1])    # axis 의 범위를 지정해준다. (보기 깔끔함)
plt.show()