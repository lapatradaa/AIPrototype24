import argparse
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()

    
    parser.add_argument(
        '--bd',
        type=int,
        required=True,
        help='birthday of the user'
    )
    
    parser.add_argument(
        '--name',
        type=str,
        default = 'Lapatrada',
        #required=True,
        help='input the name of people who are using the app'
    )

    # parser.add_argument(
    #     '--XX',
    #     type=int,
    #     default=7,
    #     help='input for XX'
    # )

    args = parser.parse_args()
    return args


def printHello(who):
    print(f"Hello World!, {who}!! ")
    
def cal_todayVbd(bd):
    td = datetime.today(birthday_str, '%Y-%m-%d').date()
    #td = datetime.today().strftime('%d')
    return bd-int(td) 

def cal_days_to_birthday(birthday_str):
    today = datetime.today().date()
    birthday = datetime.strptime(birthday_str, '%Y-%m-%d').date().replace(year=today.year)
    return ((birthday if birthday >= today else birthday.replace(year=today.year + 1)) - today).days

if __name__ == "__main__":
    input_v = parse_input()
    print('This is my first .py file.')
    printHello(input_v.name)
    print(f'your birthday is {cal_todayVbd(input_v.bd)} from today')
    
