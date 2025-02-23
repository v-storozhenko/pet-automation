"""
Модуль для создания интерактивного коммита.
"""
import subprocess

import inquirer


def _get_commit_details():
    """
    Формирование структуры коммита.
    """
    # типы коммита
    commit_type_question = [
        inquirer.List(
            'commit_type',
            message="Выберите тип коммита",
            choices=['FEATURE', 'FIX'],
        ),
    ]
    commit_type = inquirer.prompt(commit_type_question)['commit_type']

    # короткое описания
    header_question = [
        inquirer.Text(
            'header',
            message="Добавьте короткое описание (обязательно)",
            validate=lambda _, x: len(x) > 0 or "Это поле обязательно!"
        ),
    ]
    header = inquirer.prompt(header_question)['header']

    # основное описания (необязательно)
    description_question = [
        inquirer.Text(
            'description',
            message="Добавьте длинное описание (необязательно)",
            default='',
        ),
    ]
    description = inquirer.prompt(description_question)['description']

    header = f"{commit_type}: {header}"
    return header, description


def make_commit():
    """
    Сделать коммит.
    """
    header, description = _get_commit_details()

    # выполнение
    try:
        first = ['git', 'commit', '-m', header]
        if description:
            second = ['-m', description]
        else:
            second = []
        subprocess.run([*first, *second], check=True)
        print("Коммит успешно сделан!")
    except subprocess.CalledProcessError:
        print("Ошибка при выполнении коммита.")


if __name__ == "__main__":
    make_commit()
