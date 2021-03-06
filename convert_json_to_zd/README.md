Convert JSON to ZD
=====================

Конвертация файлов JSON (с определенной структурой) в формат словаря Dict (.zd)    
Данный тип словаря используется например в Android-приложении [Dictan](https://play.google.com/store/apps/details?id=info.softex.dictan)

Скрипт переводит пользовательский файл json в txt формат, а затем с помощью Windows-утилиты makezd.exe преобразует в .zd

Данный скрипт предназначен для Windows и использовался в системах Windows 10, Windows 7

Формат файла JSON
-----------------

Файл json должен представлять из себя список элементов dict, В каждом элементе должно содержаться поле title из которого берется заголовок. Из заголовков в программе Dictan формируется список. Остальные элементы показываются уже при нажатии на элементах списка.    
Название поля "title" можно заменить в переменной TITLE_KEY

### Пример:

    [
      {
        "title": "Заголовок",
        "Описание": "Этот текст будет показан в приложении после выбора заголовка",
        "Массив": [
            "Элементы массива будут показываться",
            "через запятую"
        ]
      },
      {
        "title": "Заголовок №2",
        "Описание": "В тексте можно использовать HTML теги.",
        "": "Например <i>наклонный шрифт</i>, <b>жирный шрифт</b> и др."
        " ": "Если ключ пустой или состоит из пробелов, то будет выведен только текст, без имени ключа впереди"
      }
    ]

sample_mydict.json - файл примера json файла

Использование
-------------

    python makezd_from_json.py sample_mydict.json
или    

    py makezd_from_json.py sample_mydict.json

где sample_mydict.json это Ваш json-файл 


makezd.exe
----------
Для того чтобы самостоятельно сформировать словарь, можно создать текстовый файл в UTF8. Одна строка в этом файле будет отдельной записью в которой должен быть заголовок и после двух пробелов описание. Строка может содержать HTML теги. Переводы строк &lt;br&gt;.    
Для конвертации необходимо запустить утилиту с параметрами:

    makezd.exe -cp1:65001 -cp2:65001 -lcid:25 -s myfile.txt myfile.zd


Ссылки
------


В проекте использована Windows-утилита [makezd.exe](http://www.free-dict.narod.ru/download.html)

Android-приложение Dictan можно найти в [Google Play](https://play.google.com/store/apps/details?id=info.softex.dictan) или на [4pda.ru](https://4pda.ru/forum/index.php?showtopic=240267)