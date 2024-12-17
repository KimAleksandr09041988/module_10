from threading import Lock, Thread
from random import randint
from time import sleep

class Bank:
    def __init__(self):
        self.lock_ = Lock()
        self.balance = 0

    def deposit(self):
        for _ in range(100):
            random_ = randint(50, 500)
            self.balance += random_
            if self.balance >= 500 and self.lock_.locked():
                self.lock_.release()
            print(f'Пополнение: {random_}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for _ in range(100):
            random_ = randint(50, 500)
            print(f'Запрос на {random_}')
            if random_ <= self.balance:
                self.balance -= random_
                print(f'Снятие: {random_}. Баланс: {self.balance}')
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock_.acquire()

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')