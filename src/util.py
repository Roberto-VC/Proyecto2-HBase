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


def getDataFile():
    return os.listdir('./data/')
