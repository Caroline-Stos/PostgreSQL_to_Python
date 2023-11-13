#!/usr/bin/python

import psycopg2
from config import config


def insert_paciente(paciente_id):
    """ insert a new vendor into the vendors table """
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
        pac_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return pac_id

if __name__ == '__main__':
    # insert one vendor
    insert_paciente("987654")
    # insert multiple vendors
    #insert_pacientes_list([
        #('AKM Semiconductor Inc.',),
        #('Asahi Glass Co Ltd.',),
        #('Daikin Industries Ltd.',),
        #('Dynacast International Inc.',),
        #('Foster Electric Co. Ltd.',),
        #('Murata Manufacturing Co. Ltd.',)
    #])