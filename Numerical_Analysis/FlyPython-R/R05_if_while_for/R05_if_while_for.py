# Controlling the flow of the program
# if-elif-else, while, for

# conditional statement

# x<y, x>y, x is y, x==y, x!=y, x>-y, x<=y
# x or y, x and y, not x
# x in y

# if-elif-else 
n = -2
if n<0:
    print("n is negative")
elif n<10:
    print("0 <= n < 10")
else : 
    print("n >= 10")

# or-and
i = True; j = False
k = i or j; n = i and j; m = not(i and j)
print(k,j,k,n,m)

# conditional statement
n = 10; k = n%3; m = n//3
print(n,k,m)

# loop or iteration - while
i = 1
while i < 30 :
    print(i,end=" ")
    if (i%3) == 0 :
        print(",",i)
    i = i + 1

# loop or iteration - for
for i in range(31) : 
    print(i,end=" ")
    if (i%3) == 0 :
        print(",",i)

