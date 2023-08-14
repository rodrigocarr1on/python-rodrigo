n1=int(input('ingresa un numero'))
n2=int(input('ingresa un numero'))
print('ingrese una opcion.\n\t 1.sumar.\n\t 2.restar\n\t 3.multiplicar\n\t 4.dividir')
tipo_de_operacion=int(input('operacion:'))

res=(str(n1 + n2))
if(1):
    print("resultado:" +res)

ans=(str(n1 - n2))
if(2):
    print=("resultado:" +ans)

ans2=(str(n1*n2))
if(3):
    print("resultado:" +ans2)

ans3=(str(n1//n2))
if(4):
    print("resultado" +ans3)
elif(n2>0): 
    print("resultado:" +ans3)
else:
    print("error")
