

def exemplo():
    x = 1 #int
    x = "Aula" #string
    x = 15.6 #float
    x = True #bool
    n1=5;n2=2;x=complex(n1,n2) #complex
    #print(x.real)
    #print(x.imag)

    x=["Carro","Casa","Navio",1,9.0,True] #List / Array
    x[0]= "Aviao"
    print("Valor da lista: "+x[0]) #Mostrar uma linha da list

    x=("Carro","Casa","Navio",1,9.0,True) # Tupla não é possivel modificar

    x=range(0,100,2)#Cria a lista de 2 em dois

    x={
        "casa":"2",
        "carro":"5",
        "Avião":"4"
        
    } #Dicionario com conteudo e valor
    print("Valor:"+x["casa"])

    x={2,3,4,6,8,3,6,3,4,1} #set

    x=frozenset({2,3,4,6,8,3,6,3,4,1}) #set

    print("Valor: "+str(x))
    print("tipo: "+str(type(x)))
    
    
    
fruits = ["apple", "banana", "cherry","casa","Carro"]
for x in fruits:
  if x == "cherry":
    break
  print(x)
fruits[1]="caminhao"
print(fruits)