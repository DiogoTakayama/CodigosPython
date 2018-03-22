'''
Faça um programa
que receba uma hora(uma variável para hora outra para minuto),Calcule e mostre:
a)hora digitada convertida em minutos;
b)Total de minutos,ou seja minutos digitados mais conversão anterior;
C)Total de minutos convertido em segundos.

 minutos/horas->minutos/60;
 horas->minutos->hora*60;
 segundos/minutos->segundos/60
minutos/segundos-minutos*60;
segundos/horas->segundo/3600;
 horas/segundo->horas*3600
'''


Horas=float (input("Entre com hora:"))
Minutos=float (input("Entre com minuto:"))

HorasEmMinutos = Horas*60
TotalMinutos=HorasEmMinutos+Minutos
ConversaoEmSegundos=TotalMinutos*60

print ("Hora digitada convertida em minutos: {}".format(HorasEmMinutos))
print ("Total de minutos: {}".format(TotalMinutos))
print ("Total de minutos convertido em segundos: {}".format(ConversaoEmSegundos))

