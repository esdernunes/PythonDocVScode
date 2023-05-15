import re  #Regx

texto= "Aula de curso em Python."

res=re.sub("\s","-",texto) #substituir espaço por linha


print(res)

for i in res:
    print(i)
