num=int(input("Digite um numero Para saber sua Tabuada de Soma e Multiplicacao: "))
QuantVezes=int(input("Digite a quantidade de Vezes da tabuada: "))
cont=0
print ("=== Tabuada da Multiplicacao === ")
while cont<=QuantVezes:
   tab = num * cont
   print( "%d X %d = %d" % (num, cont, tab))
   cont = cont + 1
print ("=== Tabuada da Soma === ")
x=0
while x<=QuantVezes:
   soma=(num+x)
   print ("%d + %d = %d" % (num,x,soma))
   x=x +1
  
