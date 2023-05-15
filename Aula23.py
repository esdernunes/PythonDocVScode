class Carro:
    Cor=""
    Ligado=False
    VelMax=0
    

c1=Carro()
c2=Carro()
c3=Carro()

c1.Cor="preto"
c1.Ligado=False
c1.VelMax=200

print("Velocidade Maxima: ",c1.VelMax)
print("Cor: ",c1.Cor)
estado="sim"if c1.Ligado else "Não"
print("Ligado: "+ estado)

print("Velocidade Maxima: ",c2.VelMax)
print("Cor: ",c2.Cor)
estado="sim"if c2.Ligado else "Não"
print("Ligado: "+ estado)