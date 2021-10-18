# Floatting point number
x = -12.
xh = float.hex(x)
y = float.fromhex(xh)
z = -(1+8/16+0)*2**(3)
print(x,xh,y,z)

x = 147.3
xh = float.hex(x)
y = float.fromhex(xh)
z = (1+2/16+6/16**2+9/16**3+9/16**4+9/16**5+
     9/16**6+9/16**7+9/16**8+
     9/16**9+9/16**10+9/16**11+9/16**12+10/16**13)*2**(7)
print(x,xh,y,z)

import sys
largest = sys.float_info.max
smallest= sys.float_info.min
print(largest,smallest,2**(1-1023)*(1+0))
print(4.9-4.845,4.8-4.845)
print(4.9-4.845 == 0.055, round(4.9-4.845,5)==round(0.055,5))
emach = sys.float_info.epsilon
print(emach,2**(-52))
print(1.+emach == 1, 1.+emach/2 == 1)

# Finding eps such that smallest 1+eps > 1
eps = 1.; k = 0
while 1.+eps > 1. :
    print(eps)
    eps = eps/2
    k = k+1
    # python에서 최소로 구할 수 있는 숫자는 약 2.22e-16 으로 이 값은 0으로 취급된다.
    # eps/2 의 52번째 에서 0의 값을 가진다
eps = eps*2
k = k-1 
print("Finding eps = ",eps,"at ",k)


