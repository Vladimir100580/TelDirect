PATH = 'tel_directory.txt'


def load_file():
    with open(PATH, 'r', encoding='utf8') as f:
        return list(enumerate(map(lambda x: x[:len(x) - 1], f)))


def calc_lenght():    #  Рассчет ширины столбцов и общей максимальной ширины
    with open(PATH, 'r', encoding='utf8') as f:
        f0 = list(f)
        l_num = len(str(len(list(f0))))   # учитываем длину максимального числа в нумерации списка
        u = list(zip(*map(lambda x: x.split(' '), map(lambda x: x[:len(x) - 1], f0))))  # создаем вложенные в список кортежи содержащие отдельно: имена, фамилии, телефоны и коментарии ...
        max_len = ([max([len(i) for i in arr]) for arr in u])  # создаем список с максимальной длиной имени, фамилии, тел. и комментария ... Все это для красоты ширины столбцов
        max_len.append(l_num)
        max_len.append(sum(max_len))  # добавляем сумму всех элеметнов (общую длину)
    return max_len


def create_contact(data: list[str]):
    if len(data) == 3:
        data.append('-')
    if len(data) > 4:                      # Если комментарий содержит несколько слов, - слепляются в одно, с разделителем '_'
        data[3] = '_'.join(data[3:])
        data = data[:4]
    data = ' '.join(data) + '\n'
    with open(PATH, 'a', encoding='utf8') as f:
        f.write(data)
    sort_guide_and_save()


def find_contact(substr):
    with open(PATH, 'r', encoding='utf8') as f:
        arr = []
        for sub in list(enumerate(map(lambda x: x[:len(x) - 1], f))):
            if substr.upper() in str(sub[1]).upper():    # создаем запрос не чувствительный к регистру букв
                arr.append((int(sub[0]), sub[1]))
    return arr


def edit_contact(list0: list, nom: int, cord: list):
    with open(PATH, 'w', encoding='utf8') as f1:
        for l in list0:
            if nom != int(l[0]) + 1:        # Понимаю, что со словарями было бы менее запаристо)
                f1.write(l[1] + '\n')
            else:
                st0 = l[1].split(' ')
                new_str = ''
                i = 0
                for s in cord:
                    if s == '':
                        new_str += st0[i] + ' '
                    else:
                        new_str += s + ' '
                    i += 1
                new_str = new_str[:-1] + '\n'
                f1.write(new_str)
    sort_guide_and_save()


def delete_contact(arr: list, nom: int):
    with open(PATH, 'w', encoding='utf8') as f1:
        for l in arr:
            if nom != int(l[0]) + 1:
                f1.write(l[1] + '\n')


def sort_guide_and_save():          # сортировка справочника по фамилии
    with open(PATH, 'r', encoding='utf8') as f:
        fl = list(f)
        if '\n' not in fl[-1]:       # избегаем "слепку" последней строчки с какой-либо другой при сортировке.
            fl[-1] += '\n'
        fl.sort()
    with open(PATH, 'w', encoding='utf8') as f1:
        for l in fl:
            f1.write(l)
