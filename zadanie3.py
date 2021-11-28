class Tomato:

    states = {1: "Цветение", 2: "Формирование плода", 3: "Вызревание плода"}

    def __init__(self, index):
        self._index = index
        self._state = 1

    def grow(self):
        if self._state < 3:
            self._state += 1
        self._print_state()

    def is_ripe(self):
        if self._state == 3:
            return True
        return False

    def _print_state(self):
        print(f"Помидоры {self._index} в {Tomato.states[self._state]}")

class TomatoBush:

    def __init__(self, num):
        self.tomatoes = [Tomato(index) for index in range(num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []

class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        print("Садовник приступил к работе.........")
        self._plant.grow_all()
        print("Садавник закончил свою работу!")

    def harvest(self):
        print("Садовник идет собирать урожай.....")
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Весь урожай собран!")
        else:
            print("ВНИМАНИЕ!!!! Урожай еще зеленый и не вспелый, его рано собирать!!!")

    @staticmethod
    def knowledge_base():
        print("Залог хорошей рассады и высокого урожая – качественные семена.\n"
              "Поливают рассаду томатов тонкой струей.\n"
              "Рассадные контейнеры выставляют на места с хорошим освещением.\n"
              "Удобрять помидоры можно не чаще одного раза в десять суток.\n")

if __name__ == '__main__':
    Gardener.knowledge_base()
    tomato_bush = TomatoBush(3)
    gardener = Gardener("Сергей", tomato_bush)
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.harvest()