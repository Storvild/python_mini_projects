Excel Merge
=====================

Объединение файлов Excel (или OpenOffice Calc) путем складывания значений во всех листах с выгрузкой результата в файл RESULT.xls.

Форматирование в результирующем файле при этом теряется.
    
    
Использование
-------------

Помещаем файл excel_merge.py в каталог с файлами *.xls, *.xlsx, *.ods и запускаем его
    
    python excel_merge.py
    
В результате в текущем каталоге создастся файл RESULT.xls и автоматически откроется.


Замечания
---------

Во всех файлах должны совпадать имена Листов.

По умолчанию обработка ведется начиная со второго столбца (B) второй строки (Можно изменить в переменных X_MIN, X_MAX, Y_MIN, Y_MAX)


Установка
---------
Для использования данного скрипта, необходим [Python3](https://www.python.org/downloads/) и библиотека [pyexcel](https://github.com/pyexcel/pyexcel)

Для установки расширения pyexcel выполнить в командной строке команду: 
    
    pip install pyexcel pyexcel-xls pyexcel-xlsx pyexcel-ods

или предварительно создать виртуальное окружение (Пример для Windows):

    python -m venv env_pyexcel
    env_pyexcel\Scripts\activate.bat
    pip install pyexcel pyexcel-xls pyexcel-xlsx pyexcel-ods
    
но тогда выполнять скрипт необходимо после активации виртуального окружения (env_pyexcel\Scripts\activate.bat)

или так:

    env_pyexcel\Scripts\python.exe excel_merge.py

Примечания    
----------
Данный скрипт был протестирован на Python 3.6, pyexcel==0.6.2

