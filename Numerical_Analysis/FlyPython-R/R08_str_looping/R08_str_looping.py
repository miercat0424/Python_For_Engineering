# Loop control

# String formatting
t1 = "My name is {name}, I'm {age} years old".format(name="John",age=36)
t2 = "My name is {0}, I'm {1} years old".format("Rachel",25)
t3 = "My naem is {}, I'm {} years old".format("Rachel",25)
print(t1,t2,t3,sep="\n")

name = "John"; age = 36; n1 = 1.2; n2 = 2
f1 = f"My name is {name}, I'm {age} years old."
f2 = f"My vision is {n1}, which is less than {n2}"
print(f1,f2,sep="\n")

# old style : %s, %d, %f
s1 = "My age is over %2d"%(20)
s2 = "My age is over %3d"%(30)
s3 = "My age is over %4d"%(40)
print(s1,s2,s3,sep="\n")

r1 = "My vsion is %f which is less than %d"%(1.2,2)
r2 = "My vsion is %.1f which is less than %d"%(1.2,2)
r3 = "My vsion is %.2f which is less than %d"%(1.2,2)
r4 = "My vsion is %4.3f which is less than %d"%(1.2,2)
print(r1,r2,r3,r4,sep="\n")

# Various loop control : for
A = [1,3,5,7,9]; B = [0]*5
T = (0,2,4,6,8,10)

m = [   {"name":"Peter", "age":30, "height":170},
        {"name":"Mike", "age":27, "height":180},
        {"name":"Paul", "age":52, "height":174}        ]
n = [   ("Peter",30,170),
        ("Mike",27,180),
        ("Paul",52,174) ]

for a in A:
    print(a,end="\t")
print()

for a,b in zip(A,B):
    b = a**2; c = a**3
    print(a,b,c,sep=",",end="\t")
print(); print(B)

for i in range(len(A)):
    a = A[i]; b = a**2
    B[i] = b
print(B)

for (name,age,height) in n:
    print(name+": ",age,height)

for i in range(len(m)):
    print(list(m[i].items()))
    print(list(m[i].keys()),list(m[i].values()))

for i,d in enumerate(m):
    ks = list(m[i].keys()); vs = list(m[i].values())
    for j in range(len(ks)):
        print(f"Key={ks[j]}: {vs[j]},",end = " ")
    print()

for i,d in enumerate(m):
    for j,w in enumerate(d) :
        print(f"[{i},{j}]={w}")
    print()
