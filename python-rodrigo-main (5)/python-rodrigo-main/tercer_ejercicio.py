seguir=True
while (seguir):
    print('ingrese una opcion.\n\t 1.sumar.\n\t 2.restar\n\t 3.multiplicar\n\t 4.dividir\n\t 5.tablas')
    tipo_de_operacion=int(input('operacion:'))

    if (1==tipo_de_operacion):
        n1=int(input('ingresa un numero'))
        n2=int(input('ingresa un numero'))
        res=(str(n1 + n2))
        print("resultado:" +res)


    if (2==tipo_de_operacion):
        n1=int(input('ingresa un numero'))
        n2=int(input('ingresa un numero'))
        ans=(str(n1 - n2))
        print("resultado:" +ans)

    if (3==tipo_de_operacion):
        n1=int(input('ingresa un numero'))
        n2=int(input('ingresa un numero'))
        ans2=(str(n1*n2))
        print("resultado:" +ans2)

    if (4==tipo_de_operacion):
        n1=int(input('ingresa un numero'))
        n2=int(input('ingresa un numero'))
        if (n2>0):
            ans3=(str(n1//n2))
            print("resultado" +ans3)
        else:
            print("error")
    
    if (5==tipo_de_operacion):
        n1= int(input('ingrese un numero:'))
    for numero in range (10):
        print(n1,' x ' ,numero+1,' = ', n1*(numero+1))

    
    
    respuesta=(input('desea seguir?:'))
    if (respuesta=='si'):
            seguir=True
    else:
            seguir=False