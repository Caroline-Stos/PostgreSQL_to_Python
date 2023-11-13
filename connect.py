#!/usr/bin/python
import psycopg2
from config import config

def connect():
    """ conectando ao PostgreSQL database server """
    conn = None
    try:
        # lendo os parametros de conexão
        params = config()

        # conectando ao PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
		
        # criando um cursor
        cur = conn.cursor()
        
        # executando comando sql
        cur.execute()

        # commit das mudanças
        conn.commit()
       
	    # fechando a comunicação com o PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


if __name__ == '__main__':
    connect()



