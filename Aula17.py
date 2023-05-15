import os
os.system("cls")
    #Chave/Key - Valor/value
carro={"Fabricante":"Honda",
       "Modelo":"HRV",
       "Ano":"2000",
       "Cor":"Vermelho"}

fab=carro["Fabricante"]

carro["Cor"]="preto"

print(carro["Cor"])

for x,y in carro.items():
    print(x,"-",y)
   
    print(carro[x])