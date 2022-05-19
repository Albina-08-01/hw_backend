class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f"CPU + Memory = {self.__cpu + self.__memory}"

    def __str__(self):
        return f"CPU: {self.__cpu} " \
               f"Memory: {self.__memory}"

    def __gt__(self, other):
        return self.memory > other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number='+996 777 99 88 11', call_to_number='Beeline'):
        self.sim_cards_number = sim_card_number
        self.call_to_number = call_to_number
        print(f"Идет звонок на номер {self.sim_cards_number} с сим-карты - {self.call_to_number}")

    def __str__(self):
        return f"sim cards list: {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, *sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f"Маршрут ведет в {location}\n")

    def __str__(self):
        return f"CPU: {self.cpu} " \
               f"Memory:{self.memory} " \
               f"Sim-Card: {self.sim_cards_list}"

number = [" +996 777 99 85 77"]

pentium_G4520 = Computer(4000, 12)
pentium_G4520.make_computations()

tel = Phone(1)

smartPhon = SmartPhone(1200, 9, number[0])
smartPhon2 = SmartPhone(500, 4, number[0])
smartPhon.call("+996 500 12 34 89", "Megacom")
smartPhon.use_gps("Belovodsk")

print(tel)
print(pentium_G4520)
print(pentium_G4520.make_computations())
print(smartPhon)
print(smartPhon2)
print(pentium_G4520 > smartPhon)