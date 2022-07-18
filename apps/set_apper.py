def set_apper():
    choice = ''
    lst = set()
    while choice != '-0-':
        choice = input('\n\n\nВведите значение листа: ')
        if choice != '-0-':
            lst.add(choice)
    result = '{'
    for i in lst:
        result += f"'{i}', "

    return f'{result[:-2]}' + '}'


if __name__ == '__main__':
    print(set_apper())
