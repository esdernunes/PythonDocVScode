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

#inserir       
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserir")
    except Error as ex:
        print(ex)







# nome=input("Digite o nome: ")
# telefone=input("Digite o telefone: ")
# email=input("Digite o email: ")
# vsql="INSERT INTO tb_contatos (T_NOMECONTATO,T_TELEFONECONTATO,T_EMAILCONTATO) VALUES('"+nome+"','"+telefone+"','"+email+"')"
# inserir(vcon,vsql)


#deletar
def deletar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro deletado")

# iddelete=input("Digite o ID do contato para ser deletado: ")
# vsql="DELETE FROM tb_contatos WHERE N_IDCONTATO="+iddelete+""
# deletar(vcon,vsql)


#Atualizar
def Atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as ex:
        print(ex)
    finally:
        print("Registro atualizado")
        
id=input("Digite o id: ")
nome=input("Digite o nome: ")
telefone=input("Digite o telefone: ")
email=input("Digite o email: ")


vsql="UPDATE tb_contatos SET  T_NOMECONTATO='"+nome+"',T_TELEFONECONTATO='"+telefone+"',T_EMAILCONTATO='"+email+"' WHERE N_IDCONTATO='"+id+"' "
Atualizar(vcon,vsql)


vcon.close()