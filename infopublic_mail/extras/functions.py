import sqlite3

def connect(url_db):
    conn = sqlite3.connect(url_db)
    cursor = conn.cursor()
    return cursor

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