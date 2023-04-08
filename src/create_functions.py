'''
*************************************************
Universidad del Valle de Guatemala
Diseño de Lenguajes de Programación

create_functions.py
- Funciones de creacion de data

Autores:
 - Diego Cordova: 20212
 - Roberto Vallecillos: 20441
*************************************************
'''

from .util import read_json


def exec_create_command(command: list) -> str:
    data = read_json('./data/table_status.json')
    prefix = command[0]
    # TODO implementar commandos de creacion de data

    match prefix:
        case 'create':
            pass
        case 'list':
            pass
        case 'disable':
            pass
        case 'is_enabled':
            pass
        case 'alter':
            pass
        case 'drop':
            pass
        case 'drop_all':
            pass
        case 'describe':
            pass

    return str(command)
