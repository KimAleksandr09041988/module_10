from time import time
from multiprocessing import Pool

def read_info(name):
    with open(name, 'r') as file:
        all_data = file.read().splitlines()

if __name__ == '__main__':
    list_ = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    # t1 = time()
    # for name in list_:
    #     read_info(name)
    # t2 = time()
    # print(t2 - t1)

    t1 = time()
    with Pool(4) as p:
        p.map(read_info, list_)
    t2 = time()
    print(t2 - t1)