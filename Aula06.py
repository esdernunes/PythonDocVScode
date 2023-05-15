var1=" Minha Variavel "


print(var1[0:5])  # mosta o valor da string entre os caracter 0 e 5
print("Tamanho: "+str(len(var1))) #mostra o tamanho da string na variavel var1
print(var1.strip()) # tira os espaços no inicio e fim das string
print(var1.lower().strip()) # escreve a string com valor minusculo 
print(var1.upper()) #Escreve a string com o valor maiusculo 
print(var1.replace("Minha","Sua")) #substitui valores dentro da string
a = var1.split(" ") #separa os valores da string em uma lista 
print(a[1]) #mostra o valor da string separado em lista

