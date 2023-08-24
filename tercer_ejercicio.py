seguir=True
while (seguir):
    n1=int(input('ingresa un numero'))
    n2=int(input('ingresa un numero'))
    print('ingrese una opcion.\n\t 1.sumar.\n\t 2.restar\n\t 3.multiplicar\n\t 4.dividir')
    tipo_de_operacion=int(input('operacion:'))

    if (1==tipo_de_operacion):
        res=(str(n1 + n2))
        print("resultado:" +res)


    if (2==tipo_de_operacion):
        ans=(str(n1 - n2))
        print("resultado:" +ans)

    if (3==tipo_de_operacion):
        ans2=(str(n1*n2))
        print("resultado:" +ans2)

    if (4==tipo_de_operacion):
        if (n2>0):
            ans3=(str(n1//n2))
            print("resultado" +ans3)
        else:
            print("error")
    respuesta=(input('desea seguir?:'))
    if (respuesta=='si'):
            seguir=True
    else:
            seguir=False