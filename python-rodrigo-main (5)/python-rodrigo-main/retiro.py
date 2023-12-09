import math
j1   = 3
j2=4
numero=0

print(j1)
print(j2)
print(numero)

res1=(numero)-(j1)
print("res1=",res1)
res2=(numero)-(j2)
print("res2=",res2)
    
if math.fabs(res1)==math.fabs(res2):
        print("es un empate")
elif math.fabs(res1)<math.fabs(res2):
        print("el ganador es el jugador 1")
else:
        print("el ganador es el jugador2")    
