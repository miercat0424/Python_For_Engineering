# Example - Finobacci sereies
# 1,1,2,3,5,8,13,21,34,55,89,...
from math import *

i = 1; j = 1
F = [1,1]
n = 20

for k in range(2,n+1):
        f = i+j; F.append(f)
        print(f,end=" ")
        i=j; j=f
print("\n",F)

g = F[n]/F[n-1]
print("g=",g)

h = (1+sqrt(5))/2
print("h=",h)