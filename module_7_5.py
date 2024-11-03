import os
import time

directory = '.'

for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(file_time))

        # parent directory
        # parent_dir = os.path.dirname(file_path)
        parent_dir = os.path.abspath(file_path)

        stat_info = os.stat(file) # ругается на невозможность найти определённый файл (.gitignore), в общем работает, поставленную задачу выполняет (если убрать папку с гит-файлами)
        file_size = stat_info.st_size

        print(f'Обнаружен файл: {file}, Путь: {file_path}, Размер: {file_size} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')


