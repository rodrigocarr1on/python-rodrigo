
def inicioS(usuario, pin):                                  #inicio de sesion
    inicio=False
    tarjeta=input('ingrese numero de tarjeta: ')
    for i in usuario:
        if i[0]==tarjeta:
            ndu=usuario.index(i)
            inicio=True
            pin=input('ingrese su pin: ')
            if i[1]==pin:
                inicio=True
                print('ingresando...')
                return inicio
            else:
                print('pin incorrecto')
    if inicio==False:
        print('tarjeta incorrecta')
