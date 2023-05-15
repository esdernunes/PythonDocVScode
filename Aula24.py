class Carro:
    Cor=""
    Ligado=False
    VelMax=0
    def __init__(self,v,l,c):
        self.VelMax=v
        self.Cor=c
        self.Ligado=l
    def mostrar(self):
        print("Velocidade Maxima: ",self.VelMax)
        print("Cor: ",self.Cor)
        estado="sim"if self.Ligado else "Não"
        print("Ligado: "+ estado)
        print("-----------------------------------")
    def ligar(self):
        self.ligado=True
    def desligado(self):
        self.ligado=False
    def andar(self):
        if(self.ligado):
            print("Andando")
            
        else:
            print("Carro desligado")

c1=Carro(200,False,"Perto")
c2=Carro(300,False,"Azul")
c3=Carro(400,True,"Cinza")

c1.ligar()
c2.ligar()


c1.mostrar()
c2.mostrar()
c3.mostrar()

c1.andar()
c2.andar()
c3.andar()