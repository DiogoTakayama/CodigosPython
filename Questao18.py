'''
Faça um programa que receba o raio de uma circunferência, calcule e mostre: 
O comprimento da circunferência, usando a fórmula 2*π*raio ; 
A área da circunferência, usando a fórmula π*raio^2 ; 
O volume de uma esfera com mesmo raio, usando a fórmula 4*π*raio^3/3.

'''
Pi= 3.14
Raio=float (input("Raio: "))
print ("Comprimento Da Circunferencia Eh: {:.2f}".format(2*Pi*Raio))
print ("A Area Da Circunferencia Eh: {:.2f}".format(Pi*Raio**(2)))
print ("O volume de uma esfera com mesmo Raio Eh: {:.2f}".format(4*Pi*Raio**3/3))
