class Option:
    def __init__(self, full_name, email, file_name, color):
        self.__full_name = full_name
        self.__email = email
        self.__file_name = file_name
        self.__color = color

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, value):
        self.__full_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    def __str__(self):
        return f'{self.__full_name} {self.__email} {self.__file_name} {self.__color}'


files = ['full_name.txt', 'email.txt', 'file_name.txt', 'color.txt']


def FuncOption():
    with open('MOCK_DATE.txt') as readOn:
        for i in readOn:
            stringM = i.split()
            stringM[0] += ' ' + stringM.pop(1)
            if len(stringM) > 4:
                stringM[0] += ' ' + stringM.pop(1)
            info = Option(*stringM)
            with open(files[0], 'a') as fullN:
                fullN.write(info.full_name)
                fullN.write('\r')
            with open(files[1], 'a') as emailN:
                emailN.write(info.email)
                emailN.write('\r')
            with open(files[2], 'a') as fileN:
                fileN.write(info.file_name)
                fileN.write('\r')
            with open(files[3], 'a') as colorN:
                colorN.write(info.color)
                colorN.write('\r')

def FileList():
    file = open('full_name.txt', 'w')
    file.close()

    file = open('email.txt', 'w')
    file.close()

    file = open('file_name.txt', 'w')
    file.close()

    file = open('color.txt', 'w')
    file.close()

FileList()
FuncOption()

while True:
    change = input('1- FullName and name \n 2 - Email \n 3 - File \n 4 - Color \n 5 - Exit \n Choose: ')
    if change == '5':
        print('the program is completed')
        break
    elif change == '1':
        with open('full_name.txt') as name:
            for i in name:
                print(i)
    elif change == '2':
        with open('email.txt') as email:
            for i in email:
                print(i)
    elif change == '3':
        with open('file_name.txt') as file:
            for i in file:
                print(i)
    elif change == '4':
        with open('color.txt') as color:
            for i in color:
                print(i)