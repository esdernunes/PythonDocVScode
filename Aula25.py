class NPC:
    def __init__(self,classe,nome,time,forca,municao):
        self.classe=classe
        self.nome=nome
        self.time=time
        self.forca=forca
        self.municao=municao
        self.vivo=True
        self.energia=100
    def info(self):
        print("Classe:  ",self.classe)  
        print("Nome:    ",self.nome)
        print("Time:    ",self.time)
        print("forca:   ",self.forca)
        print("Municao: ",self.municao)
        print("Vivo:    ","Sim"if self.vivo else "nao")
        print("Energia: ",self.energia)
        print("---------------------")
        
class Soldado(NPC):
    def __init__(self,classe,nome,time):
        self.classe="soldado"
        self.forca=200
        self.municao=200
        super().__init__(classe,nome,time,self.forca,self.municao)
        
class Guarda(NPC):
    def __init__(self,classe,nome,time):
        self.classe="Guarda"
        self.forca=500
        self.municao=200
        super().__init__(classe,nome,time,self.forca,self.municao)

class Elite(NPC):
    def __init__(self,classe,nome,time):
        self.classe="Elite"
        self.forca=400
        self.municao=500
        super().__init__(classe,nome,time,self.forca,self.municao)
    def inf(self):
        super().info()

s1=Guarda('Guarda','Olho Vivo',1)
s2=Soldado('Soldado','Balha na agulha',1)
s3=Elite('Elite','ninja',1)
s4=Soldado('Soldado','Super Atento',2)
s5=Elite('Elite','Olho Vivo',2)
s6=Guarda('Guarda','Samurai',2)


print('\n\033[31mClasse Guarda\033[m')
s1.info()
print('\n\033[31mClasse Soldado\033[m')
s2.info()
print('\n\033[31mClasse Elite\033[m')
s3.inf()
print('\n\033[31mClasse Guarda\033[m')
s4.info()
print('\n\033[31mClasse Soldado\033[m')
s5.inf()
print('\n\033[31mClasse Elite\033[m')
s6.info()