import os
import shutil
import threading
import sys
import logging
from time import time

def copy_file(src_path, dst_path):
    try:
        shutil.copy(src_path, dst_path)
    except Exception as e:
        print(f"Error copying file {src_path}: {e}")

def process_directory(source_dir, target_dir='dist'):
    # Перевіряємо чи існує цільова директорія, якщо ні - створюємо
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Рекурсивно обходимо всі піддиректорії та файли в джерельній директорії
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file_path = os.path.join(root, file)
            # Отримуємо розширення файлу
            extension = os.path.splitext(file)[1]
            # Створюємо піддиректорію у цільовій директорії за розширенням файлу
            target_subdir = os.path.join(target_dir, extension[1:])
            if not os.path.exists(target_subdir):
                os.makedirs(target_subdir)
            # Копіюємо файл до цільової директорії
            target_file_path = os.path.join(target_subdir, file)
            # shutil.copy(source_file_path, target_file_path)
            thread = threading.Thread(target=copy_file, args=(source_file_path, target_file_path))
            thread.start()
            thread.join()

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    timer = time()
    # Отримуємо шляхи до директорій з аргументів командного рядка
    source_dir = sys.argv[1] if len(sys.argv) > 1 else 'Downloads'
    target_dir = sys.argv[2] if len(sys.argv) > 2 else 'dist'
    process_directory(source_dir, target_dir)
    
    logging.debug(f'Done in {time() - timer}')