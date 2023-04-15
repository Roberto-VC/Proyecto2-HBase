'''
*************************************************
Universidad del Valle de Guatemala
Bases de datos 2

create_functions.py
- Funciones de creacion de data

Autores:
 - Diego Cordova: 20212
 - Roberto Vallecillos: 20441
*************************************************
'''

from .util import read_json


def _create(command: list) -> str:
    # TODO Implement create command
    table_name = command[1]
    column_families = []

    for column in command[2:]:
        column = column.replace(',', '')
        column = column.replace("'", '')
        column_families.append(column)

    pass


def _list(command: list) -> str:
    # TODO Implement list_command command
    pass


def _disable(command: list) -> str:
    # TODO Implement disable command
    pass


def _is_enabled(command: list) -> str:
    # TODO Implement is_enabled command
    pass


def _alter(command: list) -> str:
    # TODO Implement alter command
    pass


def _drop(command: list) -> str:
    # TODO Implement drop command
    pass


def _drop_all(command: list) -> str:
    # TODO Implement drop_all command
    pass


def _describe(command: list) -> str:
    # TODO Implement describe command
    pass


def exec_create_command(command: list) -> str:
    prefix = command[0]
    # TODO implementar commandos de creacion de data

    match prefix:
        case 'create':
            return _create(command)
        case 'list':
            return _list(command)
        case 'disable':
            return _disable(command)
        case 'is_enabled':
            return _is_enabled(command)
        case 'alter':
            return _alter(command)
        case 'drop':
            return _drop(command)
        case 'drop_all':
            return _drop_all(command)
        case 'describe':
            return _describe(command)
        case _:
            return f'ERROR: Command not found "{prefix}"'

    return str(command)
