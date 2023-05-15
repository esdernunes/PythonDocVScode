import re  #Regx

texto= "Aula de curso em Python."

res=re.findall("u",texto); #pesquisar valores no texto

pes=input("pesquisar: ")

res=re.findall(pes,texto);

print(res)
qtde=len(pes)

print("Qtde:"+str(qtde))

for t in res:
    print(t)