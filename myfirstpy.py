import argparse
from datetime import datetime

def parse_input():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--bd',
        type=str,
        required=True,
        help='Birthday of the user in YYYYMMDD format'
    )

    parser.add_argument(
        '--name',
        type=str,
        default='Lapatrada',
        help='Input the name of the user'
    )

    args = parser.parse_args()
    return args

def printHello(who):
    print(f"Hello World!, {who}!!")

def cal_days_from_birthday(bd):
    today = datetime.today()
    birth_date = datetime.strptime(bd, '%Y%m%d')

    if birth_date > today:
        raise ValueError("The birthday cannot be in the future!")

    delta = today - birth_date
    return delta.days

if __name__ == "__main__":
    input_v = parse_input()
    print('This is my first .py file.')
    printHello(input_v.name)
    days_from_birthday = cal_days_from_birthday(input_v.bd)
    print(f'I have been {days_from_birthday} days from your birthday!')
