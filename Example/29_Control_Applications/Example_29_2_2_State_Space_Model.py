import numpy as np
import matplotlib.pyplot as plt
import control

#   System Matrices
A = [[0,1],[-1,-3]]
B = [[0,0],[2,4]]
C = [[5,6]]
D = [[7,0]]
ssmodel = control.ss(A,B,C,D)

# Step response for the system
t , y = control.step_response(ssmodel)

print(f"\nt (Blue)   [1] : {np.shape(t)}\
    \ny (Orange) [2] : {np.shape(y)}")

plt.plot(t,y[0][0])
plt.plot(t,y[0][1])

# Convert State space model to Transfer Fuction(s)
H = control.ss2tf(ssmodel)

print(H)


plt.show()


