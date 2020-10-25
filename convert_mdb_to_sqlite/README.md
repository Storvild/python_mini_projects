Convert MDB to SQLITE
=====================

Конвертация файлов Access (*.mdb, .accdb) в sqlite3    
Данный скрипт предназначен для Windows и использовался в системах Windows 10, Windows 7

Установка
---------

Перед использованием необходимо удостовериться что в системе Windows есть драйвера ODBC    
При запуске скрипта convert_mdb_to_sqlite.py выводятся наименования драйверов. В этом списке должен присутствовать:
    Microsoft Access Driver (*.mdb, *.accdb)
Если его нет, то необходимо установить драйвера: https://www.microsoft.com/en-US/download/details.aspx?id=13255    
Если драйвер в системе называется по другому, например: "Microsoft Access Driver (*.mdb)", то необходимо в скрипте в переменной DRIVER_ODBC указать его название

Использование
-------------

    python convert_mdb_to_sqlite.py sample_mdb_2003.mdb
или    
    py convert_mdb_to_sqlite.py sample_mdb_2003.mdb

где sample_mdb_2003.mdb это Ваш файл Access

Если файл запаролен, то пароль указывается третьим параметром:
    
    python convert_mdb_to_sqlite.py sample_mdb_2003.mdb mypass
