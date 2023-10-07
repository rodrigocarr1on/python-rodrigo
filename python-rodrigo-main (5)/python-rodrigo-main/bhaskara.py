import math
a=int(input("ingrese el numero a: "))
b=int(input("ingrese el numero b: "))
c=int(input("ingrese el numero c: "))
def bhask(a,b,c):
    sol=[] #donde se guardaran las soluciones
    p1=(b*-1) #opuesto de b
    p2=((b*b)-4*a*c) #lo que se encuentra dentro de la raiz cuadrada
    p3=(2*a) #denominador
    if p2<0:
        print("no es posible realizar esta operacion")
    else:
        p4=(math.sqrt(p2)) #raiz cuadrada
        p5a=(p1+p4) #suma de los numeradores
        p5b=(p1-p4) #resta de los numeradores
        sol=[p5a/p3,p5b/p3] #las soluciones (+-)
    return sol
x=bhask(a,b,c)
print(x)