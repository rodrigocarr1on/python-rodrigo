usuario=[['123456','1232','100000','5000'],['456789','4554','400000','2500'],['789456','2585','250000','3500']]
ndu=-1
def inicioS():                                  #inicio de sesion
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
        


moneda=['1.dolares','2.pesos']
def monedaD():                       #eleccion de moneda
    print(moneda)
    resp = int(input("Seleccione la moneda:"))
    if resp ==1:
        print('ha elegido dolares')
        return 3
    elif resp ==2:
        print('ha elegido pesos')
        return 2

menu=['1.retiro','2.giro','3.ingreso','4.consulta de saldo','5.salir']
def menup():
    print(menu)
    resp=int(input('ingrese una opcion: '))
    if resp>5  or resp<0:
        print('ingrese una opcion valida')
        menup()
    return resp

def retiro1(mond):
            eleccion=mond
            resp2=int(input('cantidad: '))
            if resp2>0:
                print('operacion realizada correctamente') 
            for i in usuario:
                saldo=int(i[eleccion])-resp2
                print(saldo)
                break
def retiro2(mond):
    eleccion=mond
    resp3=int(input('cantidad:'))
    if resp3>0:
        print('operacion realizada correctamente')
        for i in usuario:
            saldo2=int(i[eleccion])-resp3
            print(saldo2)
            break

def giro1(mond):
            eleccion=mond
            respp=int(input('cantidad a transferir: '))
            if respp>0:
                print('operacion realizada correctamente') 
            for i in usuario:
                saldo=int(i[eleccion])-respp
                print(saldo)
                break

def saldo(mond):
    eleccion=mond
    return( usuario[ndu][eleccion])
    









if inicioS():
    operacion=menup()
    mon=monedaD()
    if operacion==1:
        retiro1(mon)
    elif operacion==3:
        retiro2(mon)
    elif operacion==2:
        giro1(mon)
    elif operacion==4:
        print(saldo(mon))


respuesta=(input('desea realizar otra accion?:'))
if (respuesta=='si'):
            seguir=True
else:
            seguir=False
            print('adios')