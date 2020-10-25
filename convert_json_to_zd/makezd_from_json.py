import json
import os, sys
import subprocess

JSON_FILE = ''  # Можно указать здесь json файл или передать имя файла в параметрах скрипта
TITLE_KEY = 'title'  # Основной ключ в json, по которому будет определяться заголовок


curdir = os.path.abspath(os.path.dirname(__file__))  # Вычисление каталога где лежит скрипт
os.chdir(curdir)  # Смена текущего каталога на тот, где лежит скрипт

def convert_json_to_zd(filename):

    content_js = None
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf8') as f:
            content_js = json.load(f)
    else:
        raise Exception('Файл не судествует: {}'.format(filename))
    print('Обрабатываемый файл: {}'.format(filename))
    if content_js:
        with open(filename+'.txt', 'w', encoding='utf8') as fw:
            for rec in content_js:
                res_item = rec[TITLE_KEY] + '  '
                for key in rec:
                    if key != TITLE_KEY:
                        param_name = key+': ' if key.strip() != '' else ''
                        param_value = ''
                        if type(rec[key]) == str:
                            param_value = rec[key]
                        elif type(rec[key]) == list:
                            param_value = ', '.join(rec[key])
                        res_item += '<br>' + param_name + param_value
                print(res_item)
                res_item += '\n'
                fw.write(res_item)

        curdir = os.path.abspath(os.path.dirname(__file__))
        code = subprocess.call([os.path.join(curdir, 'makezd.exe'), '-cp1:65001', '-cp2:65001', '-lcid:25', '-s',
                                             filename+'.txt', filename+'.zd'])
        print('\nОбработка завершена с кодом {}'.format(code))


if __name__ == '__main__':
    if JSON_FILE or len(sys.argv) > 1:
        filename = JSON_FILE or sys.argv[1]
    else:
        raise Exception('Не указано имя файла json')

    convert_json_to_zd(filename)
    #print('ok')

