class animal:
    def __init__(self,especie,edad):
        self.especie=especie
        self.edad=edad
    def caminar(self):
            print("caminando...")

class loro(animal):
    def __init__(self,especie, edad, ldp):
        animal.__init__(self, especie, edad)
        self.ldp=ldp

    def volar(self):
            print("volando...")
        
miloro=loro("loro","6","2")
miloro.volar()
miloro.caminar()


