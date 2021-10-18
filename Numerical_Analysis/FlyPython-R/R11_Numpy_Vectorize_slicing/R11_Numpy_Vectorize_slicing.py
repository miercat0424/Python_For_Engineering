# Numpy array : vectorization, slicing, reshape, etc
import numpy as np
from math import *

a = list(range(1,11,1))
z = [0.]*10
print(a,z,sep="\n")

A = np.array(np.arange(1,11,1))         # 1,2,...,10
B = np.array(np.arange(0.1,1.1,0.1))    # 0.1,0.2,...,1.0
print(A,B,sep="\n")

C = np.array(np.linspace(0.1,1.0,10))  # 0.1,0.2,...,10
D = np.array(np.linspace(0,1.5,16))    # .0,.1,...1.5
E = np.array(np.linspace(0,1.5,15,endpoint=False)) # .0,.1,...1.4
print(C,D,E,sep="\n")

Z = np.zeros(10)
O = np.ones((3,3))      # 3x3 array
I = np.identity(3)      # 3x3 indentity matrix
F = 5*I                 # 3x3 diagonal matrix
print(Z,O,I,F,sep="\n")

# Vectorization in possible
print(A,A**2,np.sqrt(A),sep="\n")
## print(a,a**2,np.sqrt(A),sep="\n") <- impossible

# Array indexing & slicing
a = [[11,12,13],[21,22,23],[31,32,33]]
A = np.array(a).astype(float)
print(a,A,sep="\n")
print(np.shape(A),np.shape(a))

# Numpy Support "," slicing in Matrix
print(a[0][0],a[1][2],a[2][0])
print(A[0,0],A[1,2],A[2,0])     

print("---Slicing---")
print(a[2],A[2],sep="\n")
print(a[2][:],A[2,:],sep="\n")
print(a[2][0:3],A[2,0:3],sep="\n")

print(a[:][1],A[:,1],sep="\n")
print(a[0:3][1],A[0:3,1],sep="\n") # -> Numpy can slicing on index site

# Array reshape
print("---Reshape---")
X = np.reshape(A,-1)    # -> 1 Dimension
X = X/10
print(A,X,sep="\n")
Y = np.reshape(X,np.shape(A))
print(A,X,Y,sep="\n")