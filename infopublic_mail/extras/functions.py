import sqlite3
from flask_mail import Message
from flask import render_template
from .msg_text_plain import mensagem

def connect(url_db):
    """
    Função que conecta a base de dados
    """
    conn = sqlite3.connect(url_db)
    cursor = conn.cursor()
    return cursor, conn

def cpf_retornaId(cursor, cpf):
    sql = "SELECT id FROM usuarios WHERE cpf='{}'".format(cpf)
    cursor.execute(sql)
    id = cursor.fetchone()
    return id

def consulta_id(cursor, id):
    sql_usuario = "SELECT id, cpf, nome, telefone, email, senha FROM usuarios WHERE id={}".format(id)
    sql_senha_sistema = "SELECT senha_sistema FROM users WHERE user={}".format(id)

    sql_entidades = "SELECT entidades.codigo, entidades.nome, sistemas.sistema,\
                     CASE \
	                    WHEN entidades.local = 1 THEN 'Server RD' \
	                    WHEN entidades.local = 2 THEN '50025 - TsNovo' \
	                    WHEN entidades.local = 3 THEN 'TS-Hostdime' \
                    END AS Local \
                    FROM sistemas \
                    INNER JOIN entidades ON sistemas.id = entidades.sistema \
                    INNER JOIN users ON entidades.id = users.entidade \
                    INNER JOIN usuarios ON users.user = usuarios.id \
                    WHERE usuarios.id = {}".format(id)
                    
    cursor.execute(sql_usuario)
    id, cpf, nome, telefone, email, senha = cursor.fetchone()
    cursor.execute(sql_senha_sistema)
    senha_sistema = cursor.fetchone()
    cursor.execute(sql_entidades)
    entidades = cursor.fetchall()
    usuario = dict(id=id, cpf=cpf, nome=nome, telefone=telefone,
                    email=email, senha=senha, senha_sistema=senha_sistema,
                    entidades=entidades)
    
    return usuario 

def insere_entidade_usuario(cursor, conn, **kwargs):
    sql = f"""INSERT INTO users \
            (user, senha_sistema, entidade) \
            VALUES ({kwargs['id_user']}, "{kwargs['senha']}", {kwargs['entidade']})
        """
    cursor.execute(sql)
    conn.commit()

def insere_usuario(cursor, conn, **kwargs):
    if kwargs['ativo']:
        kwargs['ativo'] = 1
    else:
        kwargs['ativo'] = 0
    if kwargs['adm']:
        kwargs['adm'] = 1
    else:
        kwargs['adm'] = 0

    sql = f"""INSERT INTO usuarios \
            (cpf, nome, telefone, RG, email, senha, ativo, adm, data_cadastro) \
            VALUES ("{kwargs['cpf']}", "{kwargs['nome']}", "{kwargs['tel']}", \
                "{kwargs['rg']}", "{kwargs['email']}", "{kwargs['senha']}", \
                    "{kwargs['ativo']}", "{kwargs['adm']}", "{kwargs['data']}")"""
    
    try:
        cursor.execute(sql)
        conn.commit()
        return True
    except:
        return False

def trata_cpf(cpf):
    novo_cpf = ''
    for c in cpf:
        if (c == '.' or c == '-'):
            c = ''
        novo_cpf += c
    return novo_cpf