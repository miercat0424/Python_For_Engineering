# Python class
# - method, init(), inherittance, overriding
# definition of class
from math import *

class member : 
    name = "None"
    age = 0
    sex = "NA"

m1 = member; m2 = member
m1.name = "Kim"; m1.age = 25
print(m1.name,m1.age)

m2.name = "Lee"; m2.age = 20
print(m1.name,m1.age,m2.name,m2.age)

del m1; del m2

# Instance of class
m1 = member(); m2 = member()
m1.name = "Kim"; m1.age = 25
print(m1.name, m1.age)
m2.name = "Lee"; m2.age = 20
print(m1.name, m1.age, m2.name, m2.age)

total = 0
class Member():
    title = "Rotary Club"
    def __init__(self,name,age,sex="NA"):
        global total
        self.name = name
        self.age  = age
        self.sex  = sex
        total    += 1
    def profile(self): return f"Name : {self.name} Age : {self.age} Sex : {self.sex}"

n1 = Member("Jeff",30); n2 = Member("Young",62,sex="M")
print(n1.name, n1.age, n1.sex, n2.name, n2.age, n2.sex)
print(n1.profile(),n2.profile(),sep="\n")
print(n1.title,n2.title)

n1.title = "Honor Club"
print(n1.title,n2.title)

# -----
n_circles = 0
class Circle():
    title = "circle"
    def __init__(self,r,x0=.0,y0=.0):
        global n_circles
        n_circles += 1
        self.R=r
        self.X=x0
        self.Y=y0
        self.S=2*pi*r
        self.A=pi*r**2
    def geom(self):
        return f"R={self.R:.1f}, C({self.X:.1f},{self.Y:.1f}, S={self.S:.1f}, A={self.A:.1f}"

C = [ Circle(k, 2*k, k**2) for k in range(20)]
for x in C : print(x.geom())
print("Total no. circles = ", n_circles)

# inherittace
class Cylinder(Circle):
    h=0.
    def volume(self):self.V=self.A*self.h
L = [ Cylinder(k,sqrt(k),k**2) for k in range(20)]
for x in L: print(x.geom())
print("Total no. circles = ",n_circles)
for x in L: x.h = 2; x.volume(); print(x.V)



