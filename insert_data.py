#!/usr/bin/python

import psycopg2
from config import config


def insert_paciente(paciente_id, nome, telefone):
    """ inserindo um novo paciente_id """
    sql = """INSERT INTO pacientes (paciente_id, nome, telefone) 
            VALUES(%s, %s, %s) RETURNING paciente_id, nome, telefone;"""
    conn = None
    paciente_id = None
    try:
        # lendo os parametros de conexao
        params = config()
        # conectando ao PostgreSQL database
        conn = psycopg2.connect(**params)
        # criando um novo cursor
        cur = conn.cursor()
        # executando o INSERT
        cur.execute(sql, (paciente_id, nome, telefone ))
        # recuperando o id gerado
        paciente_id = cur.fetchone()[0]
        # fechando a comunicação com o database
        cur.close()
        # commit das mudanças
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return paciente_id

if __name__ == '__main__':
    # insere um novo paciente_id
    insert_paciente('987655', 'Caroline','987654321')
    # insert multiplos pacientes_ids
    #insert_paciente([
        #('000001',),
        #('000002',),
        #('000003',),
        #('000000',),
        #('000000',),
        #('000000',)
    #])