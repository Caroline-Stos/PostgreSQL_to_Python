#!/usr/bin/python

import psycopg2
from config import config


def insert_paciente(paciente_id):
    """ inserindo um novo paciente_id """
    sql = """INSERT INTO pacientes(paciente_id)
             VALUES(%s) RETURNING paciente_id;"""
    conn = None
    pac_id = None
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (paciente_id,))
        # get the generated id back
        paciente_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return paciente_id

if __name__ == '__main__':
    # insere um novo paciente_id
    insert_paciente("987654")
    # insert multiplos pacientes_ids
    #insert_paciente_list([
        #('000000',),
        #('000000',),
        #('000000',),
        #('000000',),
        #('000000',),
        #('000000',)
    #])