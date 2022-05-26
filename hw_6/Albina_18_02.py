import re


def sort(file_names):
    with open(file_names, 'a', encoding='UTF=8') as fileN:

        if change == '1':
            full_name = re.findall(r"[A-Z]+[A-z]+\w+\s+[A-z]+[a-z]+\w+|[A-Z]+[A-z]+\w+\s+[A-Z][']\s+[A-z]+[a-z]+\w+",
                                   reading_file)
            fileN.write(f'{full_name} \n')
        elif change == '2':
            gmail = re.findall(r'\w+@\w+.[a-z]+', reading_file)
            fileN.write(f'{gmail} \n')
        elif change == '3':
            file = re.findall(r"[A-Z]+[a-z]+\w+[.]+[a-z]+[0-9]|[A-Z]+[a-z]+\w+[.]+[a-z]+|[A-Z]+[a-z]+[.]+[a-z]+[0-9]|",
                              reading_file)
            fileN.write(f'{file} \n')
        elif change == '4':
            color = re.findall(r"#\w+", reading_file)
            fileN.write(f'{color} \n')
        else:
            print('ERROR')


while True:
    with open('MOCK_DATA.txt', 'r', encoding='UTF-8') as directory:
        reading_file = directory.read()

        change = input('1 - Считать имена и фамилии  \n '
                       '2 - Считать все емайлы  \n '
                       '3 - Считать названия файлов \n '
                       '4 - Считать цвета \n '
                       '5 - Выход :')

        if change == '1':
            sort('names.txt')
        elif change == '2':
            sort('email.txt')
        elif change == '3':
            sort('file-names.txt')
        elif change == '4':
            sort('color.txt')
        elif change == '5':
            print('Программа закрыта!')
            break
        else:
            print('Такой опции не существует')