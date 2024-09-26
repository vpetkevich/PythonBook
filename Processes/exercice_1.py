from multiprocessing import Process  as process
from datetime import datetime as dt

def show_time():
    current_time = dt.now()
    print(f'{current_time} on the clock')

if __name__ == '__main__':
    for n in range(3):
        p = process(target=show_time)
        p.start()
