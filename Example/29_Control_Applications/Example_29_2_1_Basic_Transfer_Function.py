import numpy as np
import control

num = np.array([3])
den = np.array([4,1])

H = control.tf(num,den)

print("H(s) = " , H)