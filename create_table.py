#!/usr/bin/python

import psycopg2
from config import config

def create_tables():
    """ criando uma tabela no PostgreSQL database"""
    commands = (
        """
        CREATE TABLE pacientes (
            paciente_id SERIAL PRIMARY KEY,
            nome VARCHAR(50) UNIQUE NULL,
            telefone INT 
        )
        """,
   )
    
    conn = None
    try:
        # lendo os parametros de conexão
        params = config()
        # conectando ao PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # criando tabela uma por uma
        for command in commands:
            cur.execute(command)
        # fechando a comunicação com o PostgreSQL database server
        cur.close()
        # commit das mudanças
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    create_tables()