import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Initialization
tstart=0
tstop=25
increment=1

T=5
a= -1/T
x0= 1
t = np.arange(tstart,tstop+1,increment)


#Functionthatreturnsdx/dt
def mydiff(x,t,a):

    dxdt=a*x

    return dxdt


#SolveODE
x = odeint(mydiff,x0,t,args=(a,))
print(x)


#PlottheResults
plt.plot(t,x)
plt.title('Plotting Differential Equation Solution')
plt.xlabel("t")
plt.ylabel("x(t)")
plt.grid()
plt.axis([0,25,0,1])
plt.show()