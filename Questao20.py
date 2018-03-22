Watts=18.0
Lado1=float (input("Lado1: "))
Lado2=float (input("Lado2: "))

Area=Lado1*Lado2
Resultado=Area*Watts

if Lado1>0 and Lado2>0:

    print ("A Area do Comodo Eh:{:.2f}".format(Lado1*Lado2))
    print ("A Potencia da iluminacao do comodo Eh:{:.2f}".format(Resultado))
else:
    print ("Digite um Valor Positivo....")
