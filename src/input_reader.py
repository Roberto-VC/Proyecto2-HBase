'''
*************************************************
Universidad del Valle de Guatemala
Bases de datos 2

input_reader.py
- Lectura de comandos

Autores:
 - Diego Cordova: 20212
 - Roberto Vallecillos: 20441
*************************************************
'''

from .DDL import exec_DDL
from .manipulacion import manipulacion

DDL_COMMANDS = [
    'create',
    'list',
    'disable',
    'enable',
    'is_enabled',
    'alter',
    'drop',
    'drop_all',
    'describe'
]

DML_COMMANDS = [
    'put',
    'get',
    'scan',
    'delete',
    'deleteAll',
    'count',
    'truncate'
]


def process_input(input: str) -> str:
    if input == 'exit':
        return ''

    splited = input.split(' ')
    command = splited[0]

    if command in DDL_COMMANDS:
        return exec_DDL(splited)

    if command in DML_COMMANDS:
        return manipulacion(splited)

    return f'ERROR: comand "{input}" not valid'
