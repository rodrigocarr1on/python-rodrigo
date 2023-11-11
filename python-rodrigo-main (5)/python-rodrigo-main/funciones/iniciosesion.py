
def Login():
    nombre=input ("ingrese usuario:")
    passw=input("ingrese contraseña:")
    ingreso=[nombre,passw]
print("holalkasjdlasd")

    inicioS=False
    usuarios=[["pedro","1234"],["marta","4321"]]
    for i in usuarios:
        cont=0
        for k in range(len(i)):
            if i [k]==ingreso[k]:
                cont+=1
        if cont>1:
            inicioS=True
            print("iniciando...")
            break
    return inicioS

if Login():
    print("INICISTE BINE")
else:
    print("no")

