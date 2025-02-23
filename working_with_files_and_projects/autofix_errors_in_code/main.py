"""
Модуль для очистки и анализа Python-кода.

Этот скрипт выполняет три действия:
1. Удаляет неиспользуемые импорты с помощью `autoflake`.
2. Форматирует код в соответствии с PEP8 с помощью `autopep8`.
3. Анализирует код с помощью `pylint`.
"""

import os

import autopep8
import pylint.lint
import autoflake


def _get_python_files():
    """
    Найти все .py файлы в текущей директории (и ее вложениях).
    """
    python_files = []
    for root, dirs, files in os.walk("."):
        # "." - текущая директория и все её подкаталоги

        # игнорируем все директории, имя которых начинается с точки
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for file in files:
            if file.endswith(".py"):
                python_files.append(os.path.join(root, file))
    return python_files


def check_code():
    """
    Проверяет и форматирует все .py файлы в текущей директории.
    """
    python_files = _get_python_files()

    for file in python_files:
        # `autoflake`: удаление неиспользуемых импортов
        with open(file, "r", encoding="utf-8") as f:
            cleaned_code = autoflake.fix_code(
                f.read(),
                remove_unused_variables=True,
                remove_all_unused_imports=True
            )
        with open(file, "w", encoding="utf-8") as f:
            f.write(cleaned_code)
        print(f"Файл {file} очищен от неиспользуемых импортов.")

        # `autopep8`: автоформатирование кода
        with open(file, "r", encoding="utf-8") as f:
            formatted_code = autopep8.fix_code(
                f.read(), options={"aggressive": 1}
            )
        with open(file, "w", encoding="utf-8") as f:
            f.write(formatted_code)
        print(f"Файл {file} отформатирован.")

        # `pylint`: анализ кода
        try:
            pylint.lint.Run([file], exit=False)
        except SystemExit as e:
            print(
                f"В файле {file} обнаружены ошибки. Код выхода: {e.code}"
            )
        else:
            print(f"Файл {file} успешно прошёл проверку.")


if __name__ == "__main__":
    check_code()
