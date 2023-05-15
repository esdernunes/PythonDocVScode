import re  #Regx

texto= "Aula de curso em Python."

res=re.search("curso",texto)
#\A C


if res != None:
    print(res.start())#mostra a posição do texto na posição inicial
    print(res.end())#mostra a posição do texto na posição final
else:
    print("Não encontrado")
