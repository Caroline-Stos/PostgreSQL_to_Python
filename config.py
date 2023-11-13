#!/usr/bin/python
# Esta é uma maneira alternativa de ler um arquivo de configuração. 
from configparser import ConfigParser

# retorna um dicionário baseado na seção fornecida no arquivo .ini fornecido 
#(o padrão é database.ini e postgresql)

def config(filename='database.ini', section='postgresql'):
    # analisando .ini
    parser = ConfigParser()
    # read config file - lendo arquivo
    parser.read(filename)

    # cria uma seção padrão no postgreSQL
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return db

