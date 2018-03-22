HorasTrabalhadas=float (input("Horas Trabalhadas: "))
SalarioMinimo=float (input("Digite o Valor do Salario Minimo: "))
HorasExtras=float (input("Digite a Qtde de Horas Extras: "))
ValorHoraTrabalhada=SalarioMinimo/8
ValorHoraExtra=SalarioMinimo/4
SalarioBase=HorasTrabalhadas*ValorHoraTrabalhada
AdicionalHoraExtra=HorasExtras*ValorHoraExtra
print ("Hora Trabalhada Eh: {}".format(ValorHoraTrabalhada))
print ("Hora Extra Eh: {}".format(ValorHoraExtra))
print ("Salario Base: {}".format(SalarioBase))
print ("Adicional Horas Extras: {}".format(AdicionalHoraExtra))
print ("Salario A Receber: {}".format(SalarioBase+AdicionalHoraExtra))

