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

from .create_functions import exec_create_command
from .manipulacion import manipulacion

CREATE_COMMANDS = [
    'create',
    'list',
    'disable',
    'is_enabled',
    'alter',
    'drop',
    'drop_all',
    'describe'
]

ALTER_COMMANDS = [
    'put',
    'get',
    'scan',
    'delete',
    'deleteall',
    'count',
    'truncate'
]


def process_input(input: str) -> str:
    if input == 'exit':
        return ''

    splited = input.split(' ')
    command = splited[0]

    if command in CREATE_COMMANDS:
        return exec_create_command(splited)

    if command in ALTER_COMMANDS:
        return manipulacion(splited)

    return f'ERROR: comand "{splited}" not valid'
