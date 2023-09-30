import math
a=int(input("ingrese el numero a: "))
b=int(input("ingrese el numero b: "))
c=int(input("ingrese el numero c: "))
def bhask(a,b,c):
    sol=[]
    p1=(b*-1)
    p2=((b*b)-4*a*c)
    p3=(2*a)
    p4=(math.sqrt(p2))
    p5=(p1+p4)
    x=(p5/p3)
    print(+-x)
bhask(a,b,c)