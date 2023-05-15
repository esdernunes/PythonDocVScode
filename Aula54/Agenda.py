import os 
import sqlite3 
from sqlite3 import Error


# Conexão
def ConexaoBanco():
    caminho="H:\\Meus documentos\\Videos\\python\\PythonDoc\\Banco\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon=ConexaoBanco()

def menuPrincipal():
    os.system("cls")
    print("1 - Inserir Novo Registro")
    print("2 - Deletar Registro")
    print("3 - Atualizar Registro")
    print("4 - Consultar Registro")
    print("5 - Consultar Registro por Nome")
    print("6 - Sair")
    
    
def menuInserir():
    print("funcao1")

def menuDeletar():
    print("funcao2")


def menuAtualiza():
    print("funcao3")


def menuConsultarID():
    print("funcao4")


def menuConsultarNome():    
    print("funcao5")

    
    
    
    
    
opc=0    
while opc !=6:
    menuPrincipal()
    opc=int(input("Digite uma opção: "))
    if opc==1:
        menuInserir()
    elif opc==2:
        menuDeletar()
    elif opc==3:
        menuAtualiza()
    elif opc==4:
        menuConsultarID()
    elif opc==5:
        menuConsultarNome()
    elif opc==6:
        os.system("cls")
        print("Programa finalizado")
    else:
        os.system("cls")
        print("opção Invalida")
        os.system("pause")