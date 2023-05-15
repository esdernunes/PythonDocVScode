import os


carros=[]
carro=input("Adicione um novo carro: ")

while carro != "-1":
  carros.append(carro)
  carro=input("Adicione um novo carro: ")
  
   
os.system('cls') 
for x in carros:
    print(x)
    

print("\nFim do Loop")