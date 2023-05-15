carros=["celta","fusca","HB20","Kombe","Palio"] #cria uma lista
carros2=["ka","147"] #cria a segunda lista
carros.append("Fit") # adiciona um elemento a lista
carros.append("Polo")# adiciona um elemento a lista
carros[3]= "Fusion" # adiciona um elemento no campo 3 da lista
carros.remove("celta") # remove um elemento da lista
carros.pop() # remove o ultimo elementod da lista


carros2= carros+carros2 # adiciona todos os elementos da lista carros a os elementos da lista 2

print("Tem "+str(len(carros))+" carros na lista") #mostra quantos elementos tem na lista

print(carros)

print(carros[3]) #mostra o elemento 3 da lista 

print(carros2)