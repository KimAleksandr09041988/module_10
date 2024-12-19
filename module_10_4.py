from  threading import  Thread
from time import sleep
from random import randint
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3,10))

class Cafe:
    def __init__(self, *args):
        self.tables  = tuple(args)
        self.queue = Queue()

    def guest_arrival(self, *args):
        for guest in args:
            list_tables = []
            for table in self.tables:
                list_tables.append(table.guest)
            if None in list_tables:
                for table in self.tables:
                    if table.guest is None:
                        table.guest = guest
                        table.guest.start()
                        print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                        break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        bool_empty = True
        bool_guest = True
        while bool_empty or bool_guest:
            bool_guest = False
            for table in self.tables:
                if table.guest is not None:
                    bool_guest = True
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        table.guest.start()
                        print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
                    else:
                        table.guest = None
                        bool_empty = False
                elif table.guest is None and not self.queue.empty():
                    table.guest = self.queue.get()
                    table.guest.start()
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
            sleep(1)

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# # Заполнение кафе столами
cafe = Cafe(*tables)
# # Приём гостей
cafe.guest_arrival(*guests)
# # Обслуживание гостей
cafe.discuss_guests()