'''
João recebeu seu salário e precisa pagar duas contas atrasadas.
Por causa do atraso, ele deveria pagar
multa de 2% sobre o valor original
de cada conta. Faça um programa que receba o salário de João e o
valor original de cada uma das contas,
calcule e mostre quanto restará do salário de João
após pagar as duas contas.
'''

Salario=float (input("Digite o Salario de Joao: "))
Conta1 = float (input("Digite o Valor Original Da 1 Conta: "))
Conta2 = float (input("Digite o Valor Original Da 2 Conta: "))


print("Restara para Joao: ")
print (Salario-(Conta1*1.02)-(Conta2*1.02))
