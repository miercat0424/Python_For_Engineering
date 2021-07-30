import cmath

x = 2
y = -3

# Converting x and y into compolex number using complex()
z = complex(x,y)
print(z.real)
print(z.imag)

print(z.conjugate())

# converting complex number into polar using polar()
w = cmath.polar(z)
print(w)

