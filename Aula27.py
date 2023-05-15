import os
os.system('cls')

carros=[]

class Carros:
    nome=""
    pot=0
    velMax=0
    ligado=False
    def __init__(self,nome,pot):
        self.nome = nome
        self.pot = pot
        self.velMax = int(pot)*2
        self.ligado = False
    
    def ligar(self):
        self.Ligado=True
    def desligado(self):
        self.ligado=False
    
    def inf(self):
        print("Nome......: ",self.nome)
        print("Potencia..: ",self.pot)
        print("Vel.Maxima: ",self.velMax)
        print("Nome......: ","sim" if self.ligado==True else"nao")

def Menu ():
    os.system("cls") or None
    print("1 - Novo carro")
    print("2 - Informações do carro")
    print("3 - Excluir Carro")
    print("4 - Ligar Carro")
    print("5 - Desligar Carro")
    print("6 - Listar Carro")
    print("7 -  Sair")
    print("Quantidade de carros",len(carros))

def NovoCarro():
    os.system("cls") or None
    n=input("Nome do carro......:")
    p=input("Potencia do carro..:")
    car=Carros(n,p)
    carros.append(car)
    print("novo carro Criado")
    os.system("pause")
    
def informacoes():
    os.system("cls") or None
    n=input("Informe o numero do carro que voce deseja informações:")
    try:
        carros[int(n)].inf()
    except:
        print("Carro não existe na lista")
    os.system("pause")
    
def excluirCarro():
    os.system("cls") or None
    n=input("Informe o numero do carro que voce deseja excluir:")
    try:
       del carros[int(n)]
    except:
        print("Carro não existe na lista")
    os.system("pause")
    
    
def ligarCarro():
    os.system("cls") or None
    n=input("Informe o numero do carro que voce deseja ligar:")
    try:
        carros[int(n)].ligar()
        print("Carro ligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")

def desligarCarro():
    os.system("cls") or None
    n=input("Informe o numero do carro que voce deseja desligar:")
    try:
         carros[int(n)].desligar()
         print("Carro desligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")

def ligarCarro():
    os.system("cls") or None
    n=input("Informe o numero do carro que voce deseja desligar:")
    try:
        carros[int(n)].desligar()
        print("Carro desligado")
    except:
        print("Carro não existe na lista")
    os.system("pause")
    
def litarCarro():
    os.system("cls") or None
    p=0
    for c in carros:
        print(p,"-",c.nome)
        p=p+1
    os.system("pause")