import csv
from infopublic_mail.extras import functions

database = 'infopublic.db'

cursor, _ = functions.connect(database)

def relatorio_servidor(cursor, num_servidor):
    """Funcão que gera um documento csv a partir do numero do servidor
    juntamente com um SELECT no banco de dados."""

    sql = "SELECT nome, codigo, comentario FROM entidades WHERE local={}".format(num_servidor)
    cursor.execute(sql)
    records = cursor.fetchall()
    return records


with open('lista_local.csv', 'w', newline='', encoding='utf-8') as csvFile:
    w = csv.writer(csvFile)
    w.writerow(['entidade', 'cod', 'comentario'])
    dados = relatorio_servidor(cursor, 5)

    for row in dados:
        linha = list(row)
        w.writerow(linha)
