import datetime

def write(some_str, result):
    with open('calk.txt', 'a', encoding='utf-8') as l:
        l.write(f'{some_str} = {result}, Time: {datetime.datetime.now()}' + '\n')