def moneda():
    seguir = True
    while (seguir):
        
        moneda=['1.dolares','2.pesos']
        print(moneda)
        resp=input('ingrese una opcion:')
        print(resp)
        if resp=='1':
            print('ha elegido dolares')
            resp2=int(input('cantidad de dolares:'))
            if resp2>1:
                print('operacion realizada correctamente') #hasta aca
        else:
            print('ha elegido pesos')
            resp3=int(input('cantidad de pesos:'))
            if resp3>1:
                print('operacion realizada correctamente')
    moneda()
    respuesta=(input('desea realizar otra opcion?:'))
    if (respuesta=='si'):
        seguir=True
    else:
        seguir=False

