import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

# Initialization
tstart = 0
tstop = 25
increment = 1

x0 = 1
t = np.arange(tstart,tstop + 1 , increment)

# Function that return dx/dt
def mydiff(x,t):
    T = 5 
    a = -1/T
    dxdt = a*x
    return dxdt

# Solve ODE 
x = odeint(mydiff,x0,t)
print(x)

# Plot the Results
plt.plot(t,x)
plt.title("Plotting Differential Equation Solution")
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.axis([0,25,0,1])
plt.show()

