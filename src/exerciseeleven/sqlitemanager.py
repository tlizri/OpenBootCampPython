import os
import sqlite3 as sql3
from typing import Any


def read_config(filepath: str) -> [str, str, tuple[str, str, str], tuple[str, str, str]]:
    """Function that return database path, table name,
    column name and types from a config file
    :param filepath: path that point to config.txt
    :type filepath: str
    :return: database path, table name, columns name and columns type
    :rtype: str, str, tuple[str, str, str], tuple[str, str, str]
    """
    # Open config.txt file
    f = open(file=filepath, mode='rt')
    # Read config.txt file
    config = f.readlines()
    # Close config.txt file
    f.close()
    # Process data
    dbpath = ''
    tablename = 'False'
    colname = list()
    coltype = list()
    alumnotable = False
    for parameter in config:
        if parameter.find('database', 0, 8) != -1:
            # Take database path
            dbpath = parameter.split(sep='=')[1].replace('\n', '')
            dbpath = os.path.abspath(dbpath)
        elif parameter.find('table', 0, 5) != -1:
            # Take table name
            tablename = parameter.split(sep='=')[1].replace('\n', '')
        elif alumnotable:  # if data is from table Alumno
            # Take column names and types
            colname.append(parameter.split(sep='=')[0].replace('\n', ''))
            coltype.append(parameter.split(sep='=')[1].replace('\n', ''))
        elif parameter.find(tablename.upper(), 0, 7) != -1:
            # If readed table Name, start to take columns properties
            alumnotable = True
        elif parameter.find('\n', 0, 2) != -1:
            # If new line, stop to take columns properties
            alumnotable = False
    return dbpath, tablename, tuple(colname), tuple(coltype)


def create_connector(dbpath: str) -> sql3.Connection:
    """Function to create SQLite connector
    :param dbpath: path to database
    :type dbpath: str
    :return: connector class
    :rtype: sqlite3.Connector()
    """
    try:
        conn = sql3.connect(database=dbpath, timeout=5,
                            isolation_level='DEFERRED', check_same_thread=True,
                            factory=sql3.Connection, cached_statements=100, uri=False)
        return conn
    except sql3.Error as e:
        print(f'Error: {e} {dbpath}')
        exit(1)


def create_cursor(conn: sql3.Connection) -> sql3.Cursor:
    """Function to create cursor
    :param conn: connector object where cursor is in
    :type conn: sqlite3.Connector
    :return: cursor
    :rtype: sqlite3.Cursor
    """
    try:
        cursor = conn.cursor()
        return cursor
    except sql3.Error as e:
        print(f'Error: {e}')
        exit(1)


def close_database(conn: sql3.Connection, cursor: sql3.Cursor or None):
    """Function to close every sqlite3 objects
    :param conn: connector
    :type conn: sqlite3.Connector
    :param cursor: cursor
    :type cursor: sqlite3.Cursor
    :return: None
    :rtype: NoneType
    """
    if cursor is not None:
        cursor.close()
    conn.close()


def insert_query(table: str, column_value: {str: Any}) -> str:
    """Function to create query sentence for insert data
    :param table: table name
    :type table: str
    :param column_value: dictionary with column name as key and column value as value
    :type column_value: dict
    :return: instert query
    :rtype: str
    """
    query = f'INSERT INTO {table}('
    for key in column_value:
        query += key
        if key != list(column_value)[-1]:
            query += ', '
        else:
            # Last element
            query += ') VALUES('
    for key in column_value:
        # Check if variable is string
        if type(column_value[key]) is str:
            query += f"""'{column_value[key]}'"""
            if key != list(column_value)[-1]:
                query += ', '
            else:
                # Last element
                query += ')'
        else:
            # Transform variable type to string
            query += str(column_value[key])
            if key != list(column_value)[-1]:
                query += ', '
            else:
                # Last element
                query += ')'
    return query


def create_table_query(table: str, columns: tuple[str, str, str]) -> str:
    """Function to make a create table query sentence
    :param table: table name
    :type table: str
    :param columns: column name
    :type columns: tuple[str, str, str]
    :return: create table query sentence
    :rtype: str
    """
    query = f'CREATE TABLE {table}('
    for name in columns:
        if name == 'id':
            query += f'{name} INTEGER PRIMARY KEY'
        elif name == 'nombre':
            query += f'{name} TEXT NOT NULL'
        elif name == 'apellido':
            query += f'{name} TEXT'
        if name == list(columns)[-1]:
            query += ')'
        else:
            query += ', '
    return query


def select_query(table: str, column: str, data: Any) -> str:
    """Function to make select query sentence
    :param table: table name
    :type table: str
    :param column: column name
    :type column: str
    :param data: condition for query
    :type data: Any
    :return: select query sentence
    :rtype: str
    """
    return f"""SELECT * FROM {table} WHERE {column} = '{data}'"""


def create_database(dbpath: str, table: str, columns: tuple[str, str, str]):
    """Function to create a database if it does not exist
    :param dbpath: database path
    :type dbpath: str
    :param table: table name
    :type table: str
    :param columns: column names
    :type columns: tuple[str, str, str]
    :return: None
    :rtype: NoneType
    """
    # If database does not exist
    if not os.path.exists(dbpath):
        # Create database
        conn = sql3.connect(database=dbpath, timeout=5,
                            isolation_level='DEFERRED', check_same_thread=True,
                            factory=sql3.Connection, cached_statements=100, uri=False)
        cursor = conn.cursor()
        # Create table
        cursor.execute(create_table_query(table, columns))
        # Add NULL data
        cursor.execute(insert_query(table, dict(zip(columns, [0, '', '']))))
        conn.commit()
        close_database(conn, cursor)


def check_database(dbpath: str, table: str, columns: tuple[str, str, str]):
    """Function to check if a database exist and create if it does not
    :param dbpath: database path
    :type dbpath: str
    :param table: table name
    :type table: str
    :param columns: column names
    :type columns: tuple[str, str, str]
    :return: None
    :rtype: NoneType
    """
    if not os.path.exists(dbpath):
        create_database(dbpath, table, columns)


def exist_columns(dbpath: str, table: str, columns: tuple[str, str, str]) -> bool:
    """Function to check if columns exist in table
    :param dbpath: database path
    :type dbpath: str
    :param table: table name
    :type table: str
    :param columns: column names
    :type columns: tuple[str, str, str]
    :return: True if exist or False in case it does not
    :rtype: bool
    """
    # Check first table row
    query = select_query(table, columns[0], 0)
    conn = create_connector(dbpath)
    cursor = create_cursor(conn)
    try:
        cursor.execute(query)
        close_database(conn, cursor)
        return True
    except sql3.OperationalError:
        close_database(conn, cursor)
        return False


def check_columns_type(dbpath: str, table: str, columns: tuple[str, str, str],
                       coltype: tuple[str, str, str]) -> bool:
    """Function to check column type
    :param dbpath: database path
    :type dbpath: str
    :param table: table name
    :type table: str
    :param columns: column names
    :type columns: tuple[str, str, str]
    :param coltype: tuple with the type of the columns
    :type coltype: tuple[str, str, str]
    :return: True if correct, False if it does not
    :rtype: bool
    """
    query = 'SELECT typeof('
    for name in columns:
        query += name
        query += ')'
        if name != columns[len(columns) - 1]:
            query += ', typeof('
        else:
            query += ' '
    query += f'FROM {table} LIMIT 1'
    conn = create_connector(dbpath)
    cursor = create_cursor(conn)
    rows = cursor.execute(query)
    tipo = rows.fetchone()
    close_database(conn, cursor)
    if len(coltype) == len(tipo):
        result = [False, False, False]
        for i in range(len(tipo)):
            if coltype[i] == 'int' and tipo[i] == 'integer':
                result[i] = True
            elif coltype[i] == 'str' and tipo[i] == 'text':
                result[i] = True
        if all(result):
            return True
        else:
            return False
    else:
        return False


def check_id(dbpath: str, table: str, data: int) -> bool:
    """Function to check if the id is in table
    :param dbpath: database path
    :type dbpath: str
    :param table: table name
    :type table: str
    :param data: id
    :type data: int
    :return: False if it exists in database, True if it does not
    :rtype:
    """
    query = f"""SELECT * FROM {table} WHERE id = {data}"""
    conn = create_connector(dbpath)
    cursor = create_cursor(conn)
    rows = cursor.execute(query)
    selected = rows.fetchall()
    close_database(conn, cursor)
    return False if len(selected) > 0 else True


def insert_data(dbpath: str, table: str, columns: tuple[str, str, str], data: tuple[int, str, str]):
    """Function to insert data in a database table
    :param dbpath: database path
    :type dbpath: str
    :param table: table name
    :type table: str
    :param columns: column names
    :type columns: tuple[str, str, str]
    :param data: data to insert
    :type data: tuple[int, str, str]
    :return: None
    :rtype: NoneType
    """
    # Check if database exist
    check_database(dbpath, table, columns)
    # Check if the new id to insert is in table
    if check_id(dbpath, table, data[0]):
        query = insert_query(table, dict(zip(columns, data)))
        conn = create_connector(dbpath)
        cursor = create_cursor(conn)
        try:
            cursor.execute(query)
            conn.commit()
            close_database(conn, cursor)
        except sql3.Error as e:
            print(f'Error: {e}')
            close_database(conn, cursor)
            exit(1)
    else:
        pass
        # print(f'UNIQUE constraint failed: {table}.id')


def search_student(dbpath: str, table: str, columns: tuple[str, str, str],
                   coltype: tuple[str, str, str], name: str) -> list:
    """Function to search student in database by name
    :param dbpath: database path
    :type dbpath: str
    :param table: table name
    :type table: str
    :param columns: column names
    :type columns: tuple[str, str, str]
    :param coltype: column types
    :type coltype: tuple[str, str, str]
    :param name: name to search
    :type name: str
    :return: a list of results of the query
    :rtype: list
    """
    # Check database exist
    check_database(dbpath, table, columns)
    # Check if columns name and types are correct
    if exist_columns(dbpath, table, columns) and check_columns_type(dbpath, table, columns, coltype):
        conn = create_connector(dbpath)
        cursor = create_cursor(conn)
        rows = cursor.execute(select_query(table, columns[1], name))
        data = rows.fetchall()
        close_database(conn, cursor)
        return data
    else:
        list()
