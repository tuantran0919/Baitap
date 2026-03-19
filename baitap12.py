a1 = float(input("a1 = "))
b1 = float(input("b1 = "))
c1 = float(input("c1 = "))
a2 = float(input("a2 = "))
b2 = float(input("b2 = "))
c2 = float(input("c2 = "))

D  = a1*b2 - a2*b1
Dx = c1*b2 - c2*b1
Dy = a1*c2 - a2*c1

if D != 0:
    print("Hệ có nghiệm duy nhất:")
    print("x =", Dx/D, ", y =", Dy/D)
else:
    if Dx == 0 and Dy == 0:
        print("Hệ có vô số nghiệm")
    else:
        print("Hệ vô nghiệm")
