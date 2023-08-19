n1=int(input('ingresa un numero'))
n2=int(input('ingresa un numero'))
print('ingrese una opcion.\n\t 1.sumar.\n\t 2.restar\n\t 3.multiplicar\n\t 4.dividir')
tipo_de_operacion=int(input('operacion:'))

seguir=True
while (seguir):
    print('resultado:', n1+n2)
    respuesta=(input('desea seguir?:'))
    if (respuesta=='si'):
        seguir=True
    else:
        seguir=False