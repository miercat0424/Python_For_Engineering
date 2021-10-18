# Container : methods, slicing, range
# list of dic., dic. of containers
A = [1,2,3,4,5]; T = (1,4,6,8,10)
print(len(A),A,len(T),T)

# methods of list
A.append(6);        print(A)
A.extend([7,8]);    print(A)
A.pop();            print(A)
A.remove(1);        print(A)
A.insert(2,1);      print(A)
A.reverse();        print(A)
A.sort();           print(A)

del A[0];           print(A)

# range - interable
I = list(range(10))
J = list(range(1,10,2)) # 1,3,5,...9 1<=...<9
K = tuple(range(10,0,-2))
print(I,J,K)

L = list(K)
M = tuple(I)
print(L,M)

#slicing
IX = I[:3]; IY = I[3:8]; IZ = I[8:]; IR = I[9::-2]
print(I[:],IX,IY,IZ,IR,I[::3])
print(K[:],K[0:3])

# methods of string
a = " Hey, what's up man. Are you OK? "
b = a.upper(); c = a.strip(); d = c.replace("Hey", "Hello"); e = c.split(",")
print(a,b,c,d,e,sep="\n")


# list of dict, dict of containers
m = [ {"name":"Peter", "age":30, "height":170},
      {"name":"Mike", "age":27, "height":180},
      {"name":"Paul", "age":52, "height":174}]
n = [("Peter",30,170),("Mike",27,180),("Paul",52,174)]
print(m,n,sep="\n")

k = list(m[0].keys()); v = list(m[0].values())
print(k,v)

p = "name" in k; q = "Park" in v; r = 125 in v
print(p,q,r)

# dic of containers : data Frame
df = {"title":"club membership", "data":n, "note":"none"}
print(df["title"], df["data"], df["note"], sep="\n")