DiaNascimento=int (input("Digite o dia Nascimento: "))
MesNascimento=int (input("Digite o Mes Nascimento: "))
AnoNascimento=int (input("Digite o ano de Nascimento: "))


DiaAtual=int (input("Digite o Dia Atual: "))
MesAtual=int (input("Digite o Mes Atual: "))
AnoAtual=int (input("Digite o Ano Atual: "))

Idade=AnoAtual-AnoNascimento
Mes=Idade*12
Dias=Idade*365
Semanas=Idade*(365/7)         
    
    

print ("A idade dessa pessoa em anos Eh: %d" % (Idade))
print ("A idade dessa pessoa em Meses Eh: %d" %(Mes))
print ("A idade dessa pessoa em Dias Eh: %d" %(Dias))
print ("A idade dessa pessoa em Semanas Eh: %d" %(Semanas))
