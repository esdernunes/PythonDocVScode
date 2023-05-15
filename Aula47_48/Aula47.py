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

############# inicio Criar Tabela    #############
vsql="""CREATE TABLE tb_contatos(
            N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
            T_NOMECONTATO VARCHAR(30),
            T_TELEFONECONTATO VARCHAR(14),
            T_EMAILCONTATO VARCHAR(30)            
                    );"""

def criarTabela(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada")
    except Error as ex:
        print(ex)

criarTabela(vcon,vsql)

vcon.close()