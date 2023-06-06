from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import date
from tqdm import tqdm
from time import sleep

def bar(count):
    for i in tqdm(range(count), desc='Процесс идёт'):
        sleep(0.25)

if __name__ == '__main__':

    calculate_salary()

    get_employees()

    print(date.today())

    bar(50)