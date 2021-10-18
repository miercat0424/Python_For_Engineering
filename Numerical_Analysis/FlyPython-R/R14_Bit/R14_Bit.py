# Number in bit - world
n = 118; m = 2**31; k = -m; M = 2**32

# bin(), .bit_length()
print(n,m,k,M)
print(bin(n),bin(m),bin(k),bin(M))  # -> (2)
print(n.bit_length(),m.bit_length(),k.bit_length(),M.bit_length())
print(oct(n),oct(m),oct(k),oct(M))  # -> (8)
print(hex(n),hex(m),hex(k),hex(M))  # -> (16)

a="a"; z="z"; s="Fly Python"
ab=bytes(a,"ascii"); zb=bytes(z,"ascii")
sb=bytes(s,"utf-8")
print(ab,zb,sb)
print(*ab,*zb,*sb)

an=int.from_bytes(ab,"big")
zn=int.from_bytes(zb,"big")
sn=int.from_bytes(sb,"big")
print(an,zn,sn)
print(bin(an),bin(zn),bin(sn))

# n byte, byte ordering
nb2=n.to_bytes(2,"big"); nb4=n.to_bytes(4,"big")
print(nb2,nb4)