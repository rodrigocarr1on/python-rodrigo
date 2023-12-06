class jenga:
    def __init__(self, material, ennumerado, color, volumen, n_de_dados, armado):
        self.material=material
        self.ennumerado=ennumerado
        self.color=color
        self.columen=volumen
        self.n_de_dados=n_de_dados
        self.armado=armado
    def armarse(self):
        if self.armado==True:
            print('ya estoy armado')
        else:
            print('me armare')
            self.armado=True
        
jenga1=jenga("madera", True, "blanco", 10, 4, True)
jenga1.armarse()
jenga2=jenga("madera", True, "rojo", 10, 4, False)
jenga2.armarse()
print(jenga1.armarse)
print(jenga2.color)