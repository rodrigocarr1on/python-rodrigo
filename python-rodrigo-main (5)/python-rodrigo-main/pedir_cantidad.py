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