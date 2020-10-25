#!python3
# -*- coding: utf-8 -*-

import sys, os
import sqlite3
import decimal
import pypyodbc 


DRIVER_ODBC = 'Microsoft Access Driver (*.mdb, *.accdb)'
#DRIVER_ODBC = 'Microsoft Access Driver (*.mdb)'

def print_info(invar):
    if invar == 'PYTHON_VER':
        print('Python:', sys.version)
    elif invar == 'PYPYODBC_VER':
        print('pypyodbc ver:', pypyodbc.version)
    elif invar == 'ODBC_DRIVERS':
        print('Поддерживаемые драйвера ODBC:')
        for s in pypyodbc.drivers():
            print(s)
        
print_info('PYTHON_VER')
print_info('PYPYODBC_VER')

curdir = os.path.abspath(os.path.dirname(__file__))
print('Текущий каталог: ' + curdir)
#os.chdir(os.path.dirname(__file__))  # Работаем в текущем каталоге

mdb_types = {
             'COUNTER':'INTEGER PRIMARY KEY',
             'VARCHAR':'VARCHAR',
             'LONGCHAR':'TEXT',
             'INTEGER':'INTEGER',
             'DOUBLE':'FLOAT',
             'REAL':'FLOAT',
             'CURRENCY':'FLOAT',
             'DATETIME':'DATETIME',
             'DATE':'DATE',
             'BIT':'BOOL',
            }
def adapt_decimal(d):
    return str(d)
# Регистрируем тип decimal.Decimal для сохранения значений в sqlite
sqlite3.register_adapter(decimal.Decimal, adapt_decimal)


def sqlite_lower(val):
    return val.lower()
def sqlite_upper(val):
    return val.upper()
def sqlite_capitalize(val):
    return val[:1].capitalize()+val[1:].lower()
        
def convert_mdb_sqlite(inmdbfilename, inpassword = ''):
    mdbpath = os.path.join(curdir, inmdbfilename)
    #sqlitepath = os.path.join(curdir, os.path.splitext(inmdbfilename)[0]+'.sqlite3') # Имя файла без расширения mdb или accdb
    sqlitepath = os.path.join(curdir, inmdbfilename + '.sqlite3')  # Имя файла Access + расширение .sqlite3
    # Вывод отладочной информации
    connection_string = 'Driver={'+DRIVER_ODBC+'};Dbq='+mdbpath+';Pwd='+inpassword
    print('Источник: ' + inmdbfilename)
    print('Создаваемый файл: ' + sqlitepath)
    print('Строка подключения: ' + connection_string)
    print()
    print_info('ODBC_DRIVERS')
    try:
        with pypyodbc.connect(connection_string) as mdb:
            mdbcursor = mdb.cursor() #lowercase=False
            tables = [x['table_name'] for x in mdbcursor.tables(tableType='TABLE')]
            print('Таблицы: ', tables)

            with sqlite3.connect(sqlitepath) as sqlitedb:
                sqlitedb.create_function('lower', 1, sqlite_lower) # Заменяем функцию lower чтобы работало с русским языком
                sqlitedb.create_function('upper', 1, sqlite_upper)
                sqlitedb.create_function('capitalize', 1, sqlite_capitalize)
                for tablename in tables:
                    print('Таблица:', tablename)
                    sqlite_columns = []
                    columns = mdbcursor.columns(table=tablename)
                    print([x[0] for x in mdbcursor.description][1:])
                    for col in columns:
                        print(col[1:])
                        sqlite_type = mdb_types[col['type_name'].upper()]
                        sqlite_col = '[{}] {}'.format(col['column_name'].lower(), sqlite_type) # Обрамляем поля в квадратные скобки и указываем тип
                        if col['type_name'] in ['INTEGER', 'VARCHAR']:
                            sqlite_col += '({})'.format(col['column_size'])
                        #if col['type_name']!='COUNTER' and col['is_nullable']=='NO':
                        #    sqlite_col += ' NOT NULL'
                        sqlite_columns.append(sqlite_col)
                    sqlite_sql_create = ',\n  '.join(sqlite_columns)
                    sqlite_sql_drop = 'DROP TABLE IF EXISTS {}'.format(tablename)
                    sqlite_sql_create = 'CREATE TABLE IF NOT EXISTS [{0}] (\n  {1}\n);'.format(tablename, sqlite_sql_create)
                    print(sqlite_sql_drop)
                    print(sqlite_sql_create)
                    sqlitedb.execute(sqlite_sql_drop) # Удаляем таблицу из sqlite
                    sqlitedb.execute(sqlite_sql_create) # Создаем таблицу в sqlite
                    
                    # Заполнение данными
                    mdbcursor.execute('SELECT * FROM '+tablename)
                    data = mdbcursor.fetchall() # Получаем данные из MS Access
                    fieldnames = ['[{}]'.format(x[0]) for x in mdbcursor.description]
                    sqlite_sql_fieldnames = ','.join(fieldnames)
                    params = []
                    for fn in fieldnames:
                        params.append('?') # Создаем параметры в виде ?,?,?
                    sqlite_sql_params = ','.join(params)
                    #print('sqlite_sql_fieldnames:', sqlite_sql_fieldnames)
                    #print('sqlite_sql_params:', sqlite_sql_params)
                    sqlite_sql_del = 'DELETE FROM [{}];'.format(tablename)
                    sqlite_sql_insert = 'INSERT INTO [{}] ({}) VALUES ({});'.format(tablename, sqlite_sql_fieldnames, sqlite_sql_params)
                    print(sqlite_sql_del)
                    print(sqlite_sql_insert)
                    sqlitedb.executemany(sqlite_sql_insert, data) # Вставляем данные в sqlite
                    print()
    except Exception as e:
        raise e


if __name__ == '__main__':
    filename = 'sample_mdb_2003.mdb'
    password = ''
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    if len(sys.argv) > 2:
        password = sys.argv[2]

    convert_mdb_sqlite(filename, password)