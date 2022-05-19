class Figure:
    un = 'cm'

    def __init__(self):
        pass

    def callculateArea(self):
        pass

    def info(self):
        pass

class Circle(Figure):
    p = 3.14

    def __init__(self, radius):
        super().__init__()
        self.__radius = radius


    def callculateArea(self):
        return Circle.p * (self.__radius ** 2)


    def info(self):
        print(f'Circle: {self.__radius} {self.un} Area: {self.callculateArea()} {self.un}')


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.__side_a = side_a
        self.__side_b = side_b


    def callculateArea(self):

        return self.__side_a * self.__side_b / 2

    def info(self):
        print(f'RightTriangle: {self.__side_a} {self.un} : {self.__side_a} {self.un} Area: {self.callculateArea()} {self.un}')


Musya = Circle(1)
Laika = Circle(2)

Deizy = RightTriangle(2, 3)
Suna = RightTriangle(1, 3)
Sanu = RightTriangle(5, 3)

Cats_Dog = [Musya, Laika, Deizy, Suna, Sanu]

for i in Cats_Dog:
    i.info()