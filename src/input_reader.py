'''
*************************************************
Universidad del Valle de Guatemala
Diseño de Lenguajes de Programación

input_reader.py
- Lectura de comandos

Autores:
 - Diego Cordova: 20212
 - Roberto Vallecillos: 20441
*************************************************
'''

from .create_functions import exec_create_command

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
    'Put',
    'Get',
    'Scan',
    'Delete',
    'Deleteall',
    'Count',
    'Truncate'
]


def _read_input(input: str) -> list:
    ''' Devuelve una lista del comando y parametros del comando '''
    return input.split(' ')


def process_input(input: str) -> str:
    if input == 'exit':
        return ''

    splited = _read_input(input)
    command = splited[0]

    if command in CREATE_COMMANDS:
        return exec_create_command(command)

    if command in ALTER_COMMANDS:
        # TODO Implementar comandos de manipulacion de datos
        return command

    return f'ERROR: comand "{command}" not valid'
