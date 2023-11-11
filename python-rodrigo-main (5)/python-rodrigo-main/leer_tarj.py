def leert():
    tarjeta=input('ingrese numero de tarjeta: ')
    
    inicio=False
    usuario=[['123456','1232','$100000','USD5000'],['456789','4554','$400000','USD2500']]
    for i in usuario:
        if i[0]==tarjeta:
            inicio=True
            pin=input('ingrese su pin: ')
            if i[1]==pin:
                print('ingresando...')
                break
            else:
                print('pin incorrecto')
    if inicio==False:
            print('tarjeta incorrecta')
leert()