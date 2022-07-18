def lst_apper():
    choice = ''
    lst = []
    while choice != '-0-':
        choice = input('\n\n\nВведите значение листа: ')
        if choice != '-0-':
            lst.append(choice)
    result = '['
    for i in lst:
        result += f"'{i}', "

    return f'{result[:-2]}]'


if __name__ == '__main__':
    print(lst_apper())
