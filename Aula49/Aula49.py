import sqlite3
from sqlite3 import Error

############# Inicio Criar conexão    #############
def ConexaoBanco():
    caminho="H:\\Meus documentos\\Videos\\python\\PythonDoc\\Banco\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

############# Fim Criar conexão    #############

vcon=ConexaoBanco()

        
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserir")
    except Error as ex:
        print(ex)


nome=input("Digite o nome: ")
telefone=input("Digite o telefone: ")
email=input("Digite o email: ")
vsql="INSERT INTO tb_contatos (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES('"+nome+"','"+telefone+"','"+email+"')"
inserir(vcon,vsql)

vcon.close()