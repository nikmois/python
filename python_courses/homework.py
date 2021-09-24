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

if (x == "d"):
    e = float(input("enter e: "))
    y = float(input("enter y: "))
    x = float(input("enter x: "))
    d = A_6(y, e, x)
    print("Результат M = ", d)
elif (x == "c"):
    y = float(input("enter y: "))
    c = A_29(y)
    print("Результат F = ", c)
elif (x == "a"):
    y = float(input("enter y: "))
    x = float(input("enter x: "))
    u = float(input("enter u: "))
    a = A_22(u, y, x)
    print("Результат T = ", a)
elif (x == "o"):
    i = float(input("enter i: "))
    y = float(input("enter y: "))
    o = B_6(i, y)
    print("Результат N = ", o)
elif (x == "t"):
    h = float(input("enter h: "))
    e = float(input("enter e: "))
    y = float(input("enter y: "))
    t = B_29(h, e, y)
    print("Результат T = ", t)
elif (x == "l"):
    y = float(input("enter y: "))
    t = float(input("enter t: "))
    l = B_22(y, t)
    print("Результат N = ", l)
else:
    print("wrong choice buddy")
