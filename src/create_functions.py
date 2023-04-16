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

from .util import read_json, write_json, getDataFile
import os


def _tableExists(table_name) -> bool:
    '''Returns True if table especified as params exists in HFILE and False if not'''
    actual_files = [file.replace('.json', '') for file in getDataFile()]
    actual_files.remove('example')
    actual_files.remove('table_status')
    return table_name in actual_files


# ---- Commands Implementation ----

def _create(command: list) -> str:
    # Get table name
    table_name = command[1]
    table_name = table_name.replace(',', '')
    table_name = table_name.replace("'", '')

    if _tableExists(table_name):
        return f'  Table "{table_name}" already exists'

    # Get column families
    column_families = []

    for column in command[2:]:
        column = column.replace(',', '')
        column = column.replace("'", '')
        column_families.append(column)

    # Build new table
    new_table = [[column for column in column_families]]
    print(new_table)

    # Enable table
    _enable(filename=table_name)

    # Write Json File
    write_json(table_name, new_table)
    return f'  Created table "{table_name}"'


def _list() -> str:
    # Get Table List
    actual_files = [file.replace('.json', '') for file in getDataFile()]
    actual_files.remove('example')
    actual_files.remove('table_status')

    if len(actual_files) == 0:
        return '  Theres no tables created in HBase yet'

    # Get Build output
    tables = 'Tables in HBase:'

    for table in actual_files:
        tables += '\n  -> ' + table

    return tables


def _disable(command: list) -> str:
    '''Disables a table in HBase'''
    # Check if table exists
    table_name = command[1]
    table_name = table_name.replace("'", '')
    if not _tableExists(table_name):
        return f'  Table "{table_name}" does not exists'

    # Get Table status data
    status = read_json('./data/table_status.json')

    # Check value
    if table_name in status.keys():
        if status[table_name] == 'disabled':
            return f'  Table "{table_name}" already disabled'

    status[table_name] = 'disabled'
    write_json('table_status', status)
    return f'  Table "{table_name}" disabled'


def _enable(command: list = None, filename: str = None) -> str:
    '''Enables a table in HBase'''
    # Get Table status data
    table_name = command[1] if filename is None else filename
    table_name = table_name.replace("'", '')
    status = read_json('./data/table_status.json')

    # Check value
    if table_name in status.keys():
        if status[table_name] == 'enabled':
            return f'  Table "{table_name}" already enabled'

    # Update value
    status[table_name] = 'enabled'
    write_json('table_status', status)
    return f'  Table "{table_name}" enabled'


def _is_enabled(command: list) -> str:
    # Get Table status data
    table_name = command[1]
    table_name = table_name.replace("'", '')
    if not _tableExists(table_name):
        return f'  Table "{table_name}" does not exists'

    # Check value
    status = read_json('./data/table_status.json')
    output = f'  Table "{table_name}" '

    if status[table_name] == 'enabled':
        output += 'is enabled'
    else:
        output += 'is not enabled'

    return output


def _drop(command: list = None, filename: str = None) -> str:
    # Get table name
    table_name = command[1] if filename is None else filename
    table_name = table_name.replace("'", '')

    if not _tableExists(table_name):
        return f'  Table "{table_name}" does not exists'

    # Remove HFile of table
    os.remove(f'./data/{table_name}.json')

    # Remove from status_table
    status = read_json('./data/table_status.json')
    status.pop(table_name)
    write_json('table_status', status)

    return f'  Table "{table_name}" has been dropped'


def _drop_all() -> str:
    actual_files = [file.replace('.json', '') for file in getDataFile()]
    actual_files.remove('example')
    actual_files.remove('table_status')

    output = ''
    for file in actual_files:
        if actual_files.index(file) > 0:
            output += '\n'

        output += _drop(filename=file)

    return output


def _getColumnFams(table_name: str) -> list:
    table = read_json('./data/' + table_name + '.json')
    return table[0]


def _alter(command: list) -> str:
    # TODO Implement alter command
    # hbase> alter '<tableName>', ‘colFam’ ⇒ ‘newName’

    # Get table name
    table_name = command[1]
    table_name = table_name.replace(',', '')
    table_name = table_name.replace("'", '')

    if not _tableExists(table_name):
        return f'  Table "{table_name}" does not exists'

    # Get table name
    alter_info = ''.join(command[2:]).replace("'", '').split('=>')
    alter_type = alter_info[0]
    alter_column = alter_info[1]

    if alter_type in _getColumnFams(table_name):
        return _updateColumnFam(table_name, alter_type, alter_column)

    if alter_type == 'delete':
        return _deleteColumnFam(table_name, alter_column)

    return f'  Error: option "{alter_type}" invalid for alter'


def _deleteColumnFam(table_name: str, colum: str) -> str:
    data = read_json('./data/' + table_name + '.json')
    column_fams = data[0]
    if colum not in column_fams:
        return f'  Table "{table_name}" does not contain column family "{colum}"'

    # Delete column from description
    column_fams.remove(colum)

    # Delete from data

    for row in data[1:]:
        k = list(row.keys())[0]
        actual_row = row[k]
        fams = actual_row.keys()

        if colum in fams:
            actual_row.pop(colum)

    write_json(table_name, data)
    return f'  column family "{colum}" deleted from table "{table_name}"'


def _updateColumnFam(table_name: str, last: str, new: str) -> str:
    data = read_json('./data/' + table_name + '.json')
    column_fams = data[0]
    if last not in column_fams:
        return f'  Table "{table_name}" does not contain column family "{last}"'

    # Update column from description
    column_fams.remove(last)
    column_fams.append(new)

    # Update from data

    for row in data[1:]:
        k = list(row.keys())[0]
        actual_row = row[k]
        fams = actual_row.keys()

        if last in fams:
            last_data = actual_row[last]
            actual_row.pop(last)
            actual_row[new] = last_data

    write_json(table_name, data)
    return f'  column family "{last}" replaced with "{new}" in table "{table_name}"'


def _describe(command: list) -> str:
    # TODO Implement describe command
    pass


# ---- Command Switch ----

def exec_create_command(command: list) -> str:
    prefix = command[0]
    # TODO command = command.lower()
    # TODO implementar commandos de creacion de data
    # TODO Comentar Funciones

    match prefix:
        case 'create':
            return _create(command)
        case 'list':
            return _list()
        case 'disable':
            return _disable(command)
        case 'is_enabled':
            return _is_enabled(command)
        case 'alter':
            return _alter(command)
        case 'drop':
            return _drop(command)
        case 'drop_all':
            return _drop_all()
        case 'describe':
            return _describe(command)
        case 'enable':
            return _enable(command)
        case _:
            return f'ERROR: Command not found "{prefix}"'
