# Array File I/O - TXT vs CSV
import numpy as np

a = np.array([[11,12,13],[21,22,23]])
print(a,a.T,sep="\n")

A=np.ones((2,2))
B=np.eye(2)             # identity matrix
C=np.zeros((2,2))
D=np.diag((-3,4))
print(A,B,C,D,sep="\n")

H=np.block([A,B,C,D])           # hstack()
V=np.block([[A],[B],[C],[D]])   # hstack()
E=np.block([[A,B],[C,D]])       # hstack()
F=np.block([[A,C],[B,D]])       # hstack()
print(H,V,E,F,sep="\n")

print("---X,Y---")
X = np.array(np.arange(12,dtype=float))
Y = 50 + np.sqrt(X)
print("X        : ",X)
print("T        : ",X.T)
print("ndim     : ",X.ndim)     # X.T = Transpose
print("shape    : ",X.shape)    # X.T = Transpose
print("T.ndim   : ",X.T.ndim)   # X.T = Transpose
print("T.shape  : ",X.T.shape)  # X.T = Transpose

# Data Setting
data = np.block([X,Y])          # hstack()
print(data.shape,data,data.T,sep="\n")
print(np.reshape(data,(12,2)))

data = np.block([[X],[Y]])      # vstack()
print(data.shape,data,data.T,sep="\n")

Data = np.vstack([[X],[Y]])
print(Data.shape,Data,Data.T,sep="\n")

# Text File I/O
C = Data.T
ID = [ f"ID-(x)" for x in C[:,0]]
# print(ID)
hlist = ["ID","Score","Scaled-Score"]
header = ",".join(hlist)+"\n"       # -> Header ¸¸µé±â

f = open("test_file.txt","w")
f.write(header)
for i in range(len(ID)):
    line = f"{ID[i]},{C[i,0]},{C[i,1]}\n"
    f.write(line)
f.close()