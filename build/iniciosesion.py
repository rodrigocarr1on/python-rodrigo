usuarios=[["pedro","12345"]]
ingresado=[]

def inicioS(usuario, pin)
    res=False                                 
    usuario.append(ingresado)
    pin.append(ingresado)

    for i in usuarios:
        if i==ingresado:
            print('ingresando correctamente')
            res=True
        else:
            print('algo salio mal')
    
    return res