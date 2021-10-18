# input(), string format
a = input("Your name? ")
print("Your name is "+a)

k = input("Age? ")
print("Your age is "+k)

# input recieves string type
age = int(k)
print("Ypur age is ",age)
print(type(k),type(age))

weight = float(input("Weight? "))
print("Your weight is ",weight)


# input Data
b = input("Enter several items in csv : ")
print(b)

buff = b.split(",")
print(buff)

m = []

for t in buff :
    if t.isnumeric():
        n = int(t)
        m.append(n)
    else : 
        m.append(t.lstrip())

print(m)