import math
import random











class juego:
    def __init__(self, n_de_j, ganador, historial,numero):
        self.n_de_j=n_de_j
        self.ganador=ganador
        self.historial=historial
        self.numero=0
        fut=juego(2, ganador,historial)
        fut.ganador()

    def probabilidades(self,jugador1,jugador2):
        jugador1=random.randint(1,10)
        jugador2=random.randint(1,10)
        self.numero=random.randint(1,10)

    def ganador(self):
        class jugadores:
            def __init__(self, nombre, dorsal, probabilidad):
                self.nombre=nombre
                self.dorsal=dorsal
                self.probabilidad=probabilidad
            
        jugador1=jugadores("alberto","10", random.randint(1,10))
        jugador2= jugadores("fernando","5", random.randint(1,10))
        print(jugador1.probabilidad)
        print(jugador2.probabilidad)
        probab_programa=random.randint(1,10)
        print(probab_programa)
        
        res1=int(probab_programa)-int(jugador1.probabilidad)
        print("res1=",res1)
        res2=int(probab_programa)-int(jugador2.probabilidad)
        print("res2=",res2)
            
        if math.fabs(res1)==math.fabs(res2):
                print("es un empate")
        elif math.fabs(res1)<math.fabs(res2):
                print("el ganador es el jugador 1")
        else:
                print("el ganador es el jugador2")
    
    historial=[]
    historial.append(ganador)
    