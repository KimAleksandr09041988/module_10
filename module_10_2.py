from threading import Thread
from time import sleep

class Knight(Thread):
    enemy = 100
    counter = 0

    def __init__(self, name, power, ):
        Thread.__init__(self)
        self.name = name
        self.power = power

    # def __battle(self):
    #     while self.enemy:
    #         sleep(1)
    #         self.counter += 1
    #         self.enemy -= self.power
    #         print(f'{self.name}, сражается {self.counter} день(дня)..., осталось {self.enemy} воинов.')

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy:
            sleep(1)
            self.counter += 1
            self.enemy -= self.power
            print(f'{self.name}, сражается {self.counter} день(дня)..., осталось {self.enemy} воинов.')
        # self.__battle()
        if self.enemy <= 0:
            print(f'{self.name} одержал победу спустя {self.counter} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
