'''
*************************************************
Universidad del Valle de Guatemala
Bases de datos 2

util.py
- Funciones auxiliares

Autores:
 - Diego Cordova: 20212
 - Roberto Vallecillos: 20441
*************************************************
'''

import json
import os


def read_json(path: str) -> dict | list:
    ''' 
    Lee un archivo json o jsonArray y devuelve su contenido como un diccionario o lista
    ``path``: Path del archivo json a leer
    '''
    # JSON file
    f = open(path)
    stream = f.read()

    # Reading from file
    data = json.loads(stream)

    # Closing file
    f.close()

    return data


def write_json(filename: str, data: dict) -> str:
    ''' 
    Escribe un diccionario como json a un archivo
    ``path``: Path del archivo json a leer
    '''
    # filename adjustements
    filename = './data/' + filename + '.json'

    # Serializing json
    json_object = json.dumps(data, indent=4)

    # Writing to sample.json
    with open(filename, 'w') as outfile:
        outfile.write(json_object)

    return filename


def is_enabled(tablename: list) -> bool:
    # Check value
    status = read_json('./data/table_status.json')
    if tablename not in status.keys():
        return None
    return status[tablename] == 'enabled'

def versions(tablename) -> int:
    # Check value
    status = read_json('./data/versions.json')
    if tablename not in status.keys():
        return None
    return status[tablename]


def getDataFile():
    return os.listdir('./data/')


def disable(table_name) -> str:
    '''Disables a table in HBase'''
    # Get Table status data
    status = read_json('./data/table_status.json')

    # Check value
    if table_name in status.keys():
        if status[table_name] == 'disabled':
            return f'  Table "{table_name}" already disabled'

    status[table_name] = 'disabled'
    write_json('table_status', status)
    return f'  Table "{table_name}" disabled'

def enable(table_name) -> str:
    '''Enables a table in HBase'''
    # Get Table status data
    status = read_json('./data/table_status.json')

    # Check value
    if table_name in status.keys():
        if status[table_name] == 'enabled':
            return f'  Table "{table_name}" already enabled'

    # Update value
    status[table_name] = 'enabled'
    write_json('table_status', status)
    return f'  Table "{table_name}" enabled'