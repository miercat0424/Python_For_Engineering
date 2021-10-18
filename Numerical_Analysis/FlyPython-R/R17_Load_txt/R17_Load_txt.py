# Numpy CSV : loadtxt()
import numpy as np
import csv

X = np.array(np.arange(12,dtype=float))
Y = 50 + np.sqrt(X)
data = np.block([[X],[Y]]).T
print(data)

header = "ID,Score,Scaled Score\n"
fname  = "text.csv"
f = open(fname,"w",newline="")
w = csv.writer(f)
f.write(header)

I = [f"Np-{x}" for x in data[:,0]]

for i in range(len(I)):
    line = [I[i],data[i,0],data[i,1]]   # -> np[column,row]
    w.writerow(line)
f.close()

# Reader
f = open(fname,"r")
r = csv.reader(f)
h = next(r)
d = []
for i,line in enumerate(r):
    b = []
    for j,word in enumerate(line):
        b.append(word)
    d.append(b)
f.close()
for x in d : print(x)
D = np.array(d)
print(D)

# Numpy CSV loadtxt() -> 굳이 open하지 않아도 csv를 읽을 수 있다.
f = open(fname,"r")
r = csv.reader(f)
header = np.array(next(r))
f.close()

IDS = np.loadtxt(fname,delimiter=",",skiprows=1,dtype="str",usecols=0)
DAT = np.loadtxt(fname,delimiter=",",skiprows=1,dtype="float",usecols=(1,2))
nrows = len(IDS)

for x in header : print("%7s"%x,end="")
print()
for i in range(nrows): print("%7s %7.3f %9.3f"%(IDS[i],DAT[i,0],DAT[i,1]))