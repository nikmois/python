import math

#A_6: M=cos2y+3.6e(в степени x)
def A_6(y, e, x):
    M = math.cos(2*y) + float(3.6*e**x)
    return M
#A_29: N=3y(во второй степени) + корень из (модуль y + 1)
def A_29(y):
    N = 3*y**2 + math.sqrt(math.fabs(y + 1))
    return N
#A_22: T = sin(2u)ln(2y(во второй степени) + корень из x)
def A_22(u, y, x):
    T = math.sin(2*u)*math.log(2*y**2 + math.sqrt(x))
    return T
#B_6: L = (0.81cos*i)/ln(y + 2i(в 3 степени)
def B_6(i, y):
    L = (float(0.81)*math.cos(i))/(math.log(y + 2*i**3))
    return L
#B_29: T = (0.355h(во второй степени) - 4.355)/(e(в степени y + h) + корень из 2.7y)
def B_29(h, e, y):
    T = ((float(0.355)*h**2) - float(4.355))/((math.pow(e, y + h)) + math.sqrt(float(2.7)*y))
    return T
#B_22: S = (4.351y(в степени 3) + 2t*ln(t))/корень из (cos2y + 4.351)
def B_22(y, t):
    S = ((float(4.351)*y**3) + (2*t*math.log(t)))/math.sqrt(math.cos(2*y) + float(4.351))
    return S


firstname = input("Your name: ")
print("Hello, " + firstname)
print("d. A6")
print("c. A29")
print("a. A22")
print("o. B6")
print("t. B29")
print("l. B22")
x = input("Choose expression with typing one of these letters: ")

numbers = 0
with open("numbs.txt", "r") as file:
    r = file.read()
    lines = r.splitlines()
    for i in lines:
        numbers = i.split(",")

qwe = input("Enter fail where to write: ")

op = open(qwe, "w")

if (x == "d"):
    e = float(numbers[0])
    y = float(numbers[1])
    x = float(numbers[2])
    d = A_6(y, e, x)
    op.write("M = ")
    op.write(str(d) + "\n")
elif (x == "c"):
    y = float(numbers[3])
    c = A_29(y)
    op.write("N = ")
    op.write(str(c) + "\n")
elif (x == "a"):
    y = float(numbers[4])
    x = float(numbers[5])
    u = float(numbers[6])
    a = A_22(u, y, x)
    op.write("T = ")
    op.write(str(a) + "\n")
elif (x == "o"):
    i = float(numbers[7])
    y = float(numbers[8])
    o = B_6(i, y)
    op.write("L = ")
    op.write(str(o) + "\n")
elif (x == "t"):
    h = float(numbers[9])
    e = float(numbers[10])
    y = float(numbers[11])
    t = B_29(h, e, y)
    op.write("T = ")
    op.write(str(t) + "\n")
elif (x == "l"):
    y = float(numbers[12])
    t = float(numbers[13])
    l = B_22(y, t)
    op.write("S = ")
    op.write(str(l) + "\n")
else:
    print("wrong choice buddy")

file.close()
op.close()
