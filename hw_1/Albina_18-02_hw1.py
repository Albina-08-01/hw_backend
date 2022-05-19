#Создать класс Person с атрибутами fullname, age, is_married
#2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
#3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который был бы словарем,
# где ключ это название урока, а значение - оценка.
#4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
#5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience.
#6. Добавить в класс Teacher атрибут уровня класса salary
#7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: к стандартной
# зарплате прибавляется бонус 5% за каждый год опыта свыше 3х лет.
#8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
#9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список и
# список возвращается функцией как результат.
#10. Вызвать функцию create_student


# class Person:
#     def __init__(self, full_name, age, is_married):
#         self.full_name = full_name
#         self.age = age
#         self.is_married = is_married
#
#     def introduce_myself(self, full_name, age, is_married):
#         print(f"Меня зовут: {full_name}. Мне: {age}. Я : {is_married}")
#
#     def output(self,):
#         return f"fullname {self.full_name}"f"age {self.age}"f"is married {self.is_married}\n"
#
# class Student(Person):
#     def __init__(self, full_name, age, is_married, marks):
#         Person.__init__(self, full_name, age, is_married)
#         self.marks = marks
#
#     def average(self):
#         print(sum(self.marks))
#
# class Teacher(Person):
#     def __init__(self, full_name, age, is_married, experience=3):
#         Person.__init__(self, full_name, age, is_married)
#         self.experience = experience
#         self.salary = 12000
#
#     def Teacher_cash(self):
#         if self.experience > 3:
#             new_salary = self.salary + ((self.salary/100*5) * (self.experience-3))
#             return new_salary
#             uchilka = Teacher("Ais", 26, False, 5)
#             print(f'{uchilka.full_name} {uchilka.age} {uchilka.is_married} {uchilka.experience}')
#             print(uchilka.Teacher_cash())
#
# def create_students():
#     student1 = Student(full_name="Ais", age=22, is_married=False,
#                        marks={ "биология": 5, "физика": 4, "математика": 5, "история": 2, "русский-язык": 3, })
#     student2 = Student(full_name="Aiko", age=15, is_married=False,
#                        marks={ "биология": 4, "физика": 5, "математика": 2, "история": 5, "русский-язык": 4, })
#     student3 = Student(full_name="Nik", age=19, is_married=False,
#                        marks={ "биология": 5, "физика": 5, "математика": 5, "история": 4, "русский-язык": 2, })
#     resultu = [student1, student2, student3]
#     return resultu
#
# students = create_students()
# for i in students:
#     list = []
# for marks in i.marks.values():
#     list.append(marks)
#     print(f"Name: {i.full_name}\n" f"Age: {i.age}\n" f"Maried: {i.is_married}\n" f"Average marks: {sum(list)/len(list)}\n")





class Person:
    def __init__(self, f, a, im):
        self.fullname = f
        self.age = a
        self.is_married = im

    def introduce_yourself(self):
        return (f'FullName: {self.fullname} \n'
                f'Age: {self.age} \n'
                f'Married: {self.is_married} ')

man = Person('Aiko', 24, False)

class Student(Person):
    def __init__(self, f, a, im, marks: dict):
        Person.__init__(self, f, a, im)
        self.marks = marks

    def introduce_yourself(self):
        return (f'FullName: {self.fullname} \n'
                f'Age: {self.age} \n'
                f'Married: {self.is_married} ')

    def get_marks(self):
        return self.marks

    def get_am(self):
        return int(sum(self.marks.values())/3)

st1 = Student('Esen', 13, False, dict(matha = 5, physics= 5,english = 5))


class Teacher(Person):
    salary = 6000
    def __init__(self, f, a, i, e):
        Person.__init__(self, f, a, i)
        self.experience = e


    def introduce_yourself(self):
        return (f'FullName: {self.fullname} \n'
                f'Age: {self.age} \n'
                f'Married: {self.is_married} \n'
                f'Experience: {self.experience} ')

    def salary_count(self):
        if self.experience > 3:
            return ((Teacher.salary) + (self.experience - 3) * t)
        else:
            return Teacher.salary


def create_students():
    st2 = ('Aiko', 14, False, {'matha':5 ,'physics': 5 , 'english': 5})
    st3 = ('Ais', 14, False, dict(matha=3, physics=4, english=5))
    st4 = ('Nik', 14, False, dict(matha=4, physics=4, english=5))
    return list([st2, st3, st4])


for func in [create_students]:
    s = func()
    print(s)

teach1 = Teacher("Aleksey", 37, True, 4)
t = (Teacher.salary / 100) * 5

print(man.introduce_yourself())
print(st1.introduce_yourself())
print(st1.get_marks())
print(f'Avarage mark: {st1.get_am()}')
print(teach1.introduce_yourself())
print(f'Teachers salary: {int(teach1.salary_count())}')