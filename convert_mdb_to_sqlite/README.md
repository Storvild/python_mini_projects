Convert MDB to SQLITE
=====================

Конвертация файлов Access (*.mdb, .accdb) в sqlite3

Использование
-------------

    python convert_mdb_to_sqlite.py sample_mdb_2003.mdb
или
    py convert_mdb_to_sqlite.py sample_mdb_2003.mdb

где sample_mdb_2003.mdb это Ваш файл Access

Если файл запаролен, то пароль указывается третим параметром
    
    python convert_mdb_to_sqlite.py sample_mdb_2003.mdb mypass
