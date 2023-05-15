import re  #Regx

texto= "Aula de curso em Python."

res=re.split("\s",texto)

print(res)
print(res[2])

for i in res:
    print(i)