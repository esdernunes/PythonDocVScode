
nome="teste"
f=open("H:/Meus documentos/Videos/python/Curso de Python/PythonDoc/Aula44/"+nome+".txt","at")

#r - read - Leitura
#w - write - Escrita
#x - write - criar
#a - append - Anexar
#t - texto
#b -binario

txt=input("Digite um texto: ")
f.write("\n"+txt+"\n")

# f.write("Curso de Python!\n Aula com escrita em arquivo")


f.close #Fechar no final
