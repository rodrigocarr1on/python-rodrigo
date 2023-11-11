
tarjeta=input('ingrese numero de tarjeta: ')
    
inicio=False
usuario=[['123456','1232','100000','5000'],['456789','4554','400000','2500']]
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
            
menu=['1.retiro','2.giro','3.ingreso','4.consulta de saldo','5.salir']
print(menu)
resp=input('ingrese una opcion: ')
if resp=='1':
    
        seguir = True
        while (seguir):
            moneda=['1.dolares','2.pesos']
            print(moneda)
            resp=input('ingrese una opcion:')
            if resp=='1':
                def monedaD():
                    print('ha elegido dolares')
                    return 3
                eleccion=monedaD()
                resp2=int(input('cantidad de dolares:'))
                if resp2>0:
                        print('operacion realizada correctamente') 
                for i[0] in usuario:
                        saldo=int(i[eleccion])-resp2
                        print(saldo)
                        break
            if resp=='2':
                def monedaP():
                    print('ha elegido pesos')
                    return 2
                eleccion2=monedaP()
                resp3=int(input('cantidad de pesos:'))
                if resp3>0:
                        print('operacion realizada correctamente')
                for i[0] in usuario:
                    saldo2=int(i[eleccion2])-resp3
                    print(saldo2)
                    break
            respuesta=(input('desea realizar otra opcion?:'))
            if (respuesta=='si'):
                            seguir=True
            else:
                            seguir=False