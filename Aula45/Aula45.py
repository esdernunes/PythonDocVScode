import re
nome="teste"
f=open("H:/Meus documentos/Videos/python/PythonDoc/Aula45/"+nome+".txt","rt")

#r - read - Leitura
#w - write - Escrita
#x - write - criar
#a - append - Anexar
#t - texto
#b -binario


for l in f:
    print(l)
    
    
print(f.readline()) # imprime linha



print(f.read(10)) # imprime 10 primeiro caracter


# f.write("Curso de Python!\n Aula com escrita em arquivo")

res=re.sub("\s","-",f.readline())

f.close #Fechar no final



f=open("H:/Meus documentos/Videos/python/PythonDoc/Aula45/"+nome+".txt","wt")
f.write(res)
f.close()

print(res)


