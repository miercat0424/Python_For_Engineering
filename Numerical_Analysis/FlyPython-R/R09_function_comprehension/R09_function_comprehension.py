# User Function
# List Comprehension

from math import *
#___ Cylinder surface area and volume
def my_cylinder(r,h):
    S = 2*pi*r*h + 2*pi*r**2
    V = pi*r**2*h
    return S,V

fn = my_cylinder
print(my_cylinder(2,4),fn(h=4,r=2))

# stress = K*strain**n
K = 965; n = 0.203
m = 20

for i in range(0,m+1):      # i = 0,1,...20
    x = float(i)/1000       # x = 0,0.001,...0.02
    y = K*x**n
    print("%.3f,%6.1f"%(x,y))

def stress(strain):
    return K*strain*n

print("---stress-strain curve")
for i in range(0,m+1):      # i = 0,1,...20
    x = float(i)/1000       # x = 0,0.001,...0.02
    y = stress(x)
    print("%.3f,%6.1f"%(x,y))

# List comprehension
X = [float(i)/1000 for i in range(0,m+1)]
Y = [stress(float(i)/1000) for i in range(0,m+1)]

print("--- X vs Y ---")
#print(X,y,sep="\n")

for x,y in zip(X,Y):
    print("%.3f,%6.1f"%(x,y))

# Comprehension for dictionary
D1 = {"a":1, "b":2, "c":3, "d":4}
D2 = {key:val**3 for (key,val) in D1.items()}
print(D1,D2,sep="\n")

print("--- Key vs Val ---")
S = ["%.3f"%(float(i)/1000) for i in range(0,m+1)]
V = [ stress(float(S[i])) for i in range(0,m+1)]
D = dict(zip(S,V))
print(D)
for key,val in D.items():
    print("%s,%6.1f"%(key,val))
