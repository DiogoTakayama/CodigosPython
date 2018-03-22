'''
Faça um programa que receba o
valor dos catetos de um triângulo retângulo,
calcule e mostre o valor da hipotenusa. Sabe-se que h=a2+b2 ,
sendo h a hipotenusa, a e b os catetos do triângulo.

'''
CatetoA=float (input("a: "))
CatetoB=float (input("b: "))
QuadradoA=CatetoA*CatetoA
QuadradoB=CatetoB*CatetoB
SomaQuadrados=QuadradoA+QuadradoB
Raiz=SomaQuadrados**(1/2)

print ("A Hipotenusa Eh:{:.2f}".format((Raiz)))
 
