import json

with  open('H:/Meus documentos/Videos/python/Curso de Python/PythonDoc/Aula39/jogador.json') as f:
    jogador=json.load(f)

def linha():
    print("---------------------------------------------------")

#chaves
for c in jogador:
    print(c)
linha()  

#itens
for c in jogador.items():
    print(c)
linha()  
    

 #valores
for c in jogador.values():
    print(c)
linha()  
       
       
#nome
print(jogador["nome"])
linha()  

#itens da mochila
for c in jogador["mochila"]:
    print(c)
linha()  
    
    
#todas as aeronaves 
for a in jogador["aeronaves"]:
    print(a)
linha()  
    
#itens
for c in jogador["aeronaves"]:
    print(c["tipo"],a["habilidade"])
linha()  
    