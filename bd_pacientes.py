import psycopg2

conexao = psycopg2.connect(database = "pacientes",
                           host = "localhost",
                           user = "postgres",
                           password = "12345",
                           port = "5432")
print(conexao.info)
print(conexao.status)




