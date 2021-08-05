import matplotlib.pyplot as plt     # MATLAB plotting functions

from control.matlab import *        # MATLAB-like function

#   Parameters defining the system
m = 250.0       #   system mass
k = 40.0        #   spring constant
b = 120.0        #   damping constant

#   System matrices
A = [[0,1.],[-k/m,-b/m]]
B = [[0],[1/m]]
C = [[1.,0]]
sys = ss(A,B,C,0)

# Step response for the system
plt.figure(1)
yout , T = step(sys)
plt.plot(T.T,yout.T)

# Bode plot for the system
plt.figure(2)
mag , phase , om = bode(sys)

plt.show()