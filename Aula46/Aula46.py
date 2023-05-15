import re
import os
nome="teste"
caminho=("H:/Meus documentos/Videos/python/PythonDoc/Aula46/"+nome+".txt")


if os.path.exists(caminho):
    print("Arquivo existente")
else:
    f=open(caminho,"tx")
    print("Arquivo criado")
    f.close()
#r - read - Leitura
#w - write - Escrita
#x - write - criar
#a - append - Anexar
#t - texto
#b -binario


if os.path.exists(caminho):
    #os.remove(caminho)
    print("Arquivo removido")
else:
    print("Arquivo inexistente")
    


