import json

jogador_j='{"nome":"Bruno","time":"aviadores","vivo":"True","energia":100,"mochila":["perdeneira","corda","linha","arame"],"aeronaves":[{"tipo":"transporte","habilidade":80},{"tipo":"ataque","habilidade":100},{"tipo":"reconhencimento","habilidade":50}]}'

jogador=json.loads(jogador_j)

#chaves
for c in jogador:
    print(c)
    
#itens
for c in jogador.items():
    print(c)
    

 #valores
for c in jogador.values():
    print(c)
       
       
#nome
print(jogador["nome"])

#itens da mochila
for c in jogador["mochila"]:
    print(c)
    
    
#todas as aeronaves 
for a in jogador["aeronaves"]:
    print(a)
    
#itens
for c in jogador["aeronaves"]:
    print(c["tipo"],a["habilidade"])
    