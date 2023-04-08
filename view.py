from typing import List

import text_fields as tx


def main_menu():
    print('''Выберите необходимое действие: 
    1. Просмотреть контакты
    2. Создать контакт
    3. Найти контакт
    4. Изменить контакт
    5. Удалить контакт
    6. Выход''')
    while True:
        n = input('Введите цифру: ')
        if n.isdigit() and 0 < int(n) < 7:
            return int(n)
        else:
            print_mes(tx.input_restriction, 0)


def print_mes(st: str, f: int):    # f - флаг указывающий на присутствие в конце запроса нажатия на "Enter" для продолжения
    if st != '':
        print('\n' + '-' * (len(st) + 2))
        print(f' {st} ')
        print('-' * (len(st) + 2) + '\n')
    if f != 0:
        input("Нажмите 'Enter' для продолжения...")


def enter_cont() -> list[str]:
    print('\nВведите Фамилию, Имя, номер телефона, комментарий(при необходимости).')
    data = input("Через пробелы: ").split()
    return data


def enter_find_str() -> str:
    print()
    substr = input('Введите подстроку для поиска: ')
    return substr


def enter_numb() -> int:
    print()
    num = int(input('Введите интересующий Вас номер контакта: '))
    return num


def enter_edit_contact() -> list:
    print('Введите новые данные контакта. Если поле не изменяется, нажимайте Ввод\n')
    f = input('Фамилия: ').strip()
    n = input('Имя: ').strip()
    nt = input('Телефон: ').strip()
    c = input('Комментарий: ').strip().replace(' ', '_')
    return[f, n, nt, c]


def show_dir(list0: list, lengths: list):
    if list0 != [] and list0[0][1] != '':
        print('\n' + (lengths[5] + 13) * '-')     # учитываем отступы
        for sub in list0:
            list1 = sub[1].split(' ')
            print(f' {int(sub[0]) + 1}.'
                  f' {list1[0]:<{lengths[0] + 2}}'
                  f' {list1[1]:<{lengths[1] + 2}}'
                  f' {list1[2]:<{lengths[2] + 2}}'
                  f' {list1[3]:<{lengths[3] + 2}}')  # каждый столбец будет на 2 символа шире максимальной длины слова в этом столбце
        print((lengths[5] + 13) * '-' + '\n')
    else:
        if lengths == [1, 1]:             # Отладка при пустом списке
            print_mes(tx.dir_empty, 1)
        else:
            print_mes(tx.find_null, 1)
