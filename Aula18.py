import random
import os

erros=0
sorteado = random.randrange(0,10)

 
numjogado=int(input("Digite seu numero: "))

while numjogado != sorteado:
    print("Você errou tente novamente")
    if(sorteado<numjogado):
        print("Erro é um numero menor")
    if(sorteado>numjogado):
        print("Erro é um numero maior")
    
    erros=erros+1
    numjogado=int(input("Digite seu numero: "))

print("Você errou ",erros, " vezes!")