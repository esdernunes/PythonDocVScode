import os
os.system("cls")

carros=[["Modelo","HRV"],
        ["Fabricante","Honda"],
        ["Ano",2022]] #Array / List

carros[0][1] = "Celta"

carros.append(["Cor","Prata"])

print(carros[2][0])

for x,y in carros:
    print (x,"-",y)
    
    