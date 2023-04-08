'''
*************************************************
Universidad del Valle de Guatemala
Diseño de Lenguajes de Programación

util.py
- Funciones auxiliares

Autores:
 - Diego Cordova: 20212
 - Roberto Vallecillos: 20441
*************************************************
'''

import json


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
