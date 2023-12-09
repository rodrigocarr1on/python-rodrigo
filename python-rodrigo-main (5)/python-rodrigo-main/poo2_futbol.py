import math
import random


class jugadores:
            def __init__(self, nombre, dorsal, probabilidad):
                self.nombre=nombre
                self.dorsal=dorsal
                self.probabilidad=probabilidad

jugador1=jugadores("alberto","10", random.randint(1,10))
jugador2= jugadores("fernando","5", random.randint(1,10))




class juego:
    def __init__(self, n_de_j, historial):
        self.n_de_j=n_de_j
        self.nombreGanador=""
        self.historial=historial
        self.numero=0


    def probabilidades(self):
        self.numero=random.randint(1,10)
        return[random.randint(1,10),random.randint(1,10)]
    
    def ganador(self,j1,j2,n1,n2):
            
        print(j1)
        print(j2)
        print(self.numero)
        
        res1=(self.numero)-(j1)
        print("res1=",res1)
        res2=(self.numero)-(j2)
        print("res2=",res2)
            
        if math.fabs(res1)==math.fabs(res2):
                print("es un empate")
        elif math.fabs(res1)<math.fabs(res2):
                self.nombreGanador=n1
        else:
                self.nombreGanador=n2 
        self.historial.append(juego1.nombreGanador)

historial=[]

juego1=juego(2,historial)

probs=juego1.probabilidades()
print(probs)
jugador1.probabilidad=probs[0]
jugador2.probabilidad=probs[1]
juego1.ganador(jugador1.probabilidad,jugador2.probabilidad,jugador1.nombre,jugador2.nombre)
print("el ganador es",juego1.nombreGanador)

print(juego1.historial)




