print('ingrese una opcion.\n\t 1.sumar.\n\t 2.restar\n\t 3.multiplicar\n\t 4.dividir\n\t 5.tablas')
tdo=int(input('operacion:'))

if(1==tdo):
    n1=int(input('ingresa un numero'))
    n2=int(input('ingresa un numero'))
    res=(str(n1+n2))
    print("resultado:" +res)