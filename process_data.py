import json
import sys

from print_result import print_result
from unique import Unique
from gen_random import gen_random
from cm_timer import cm_timer_1

# Сделаем другие необходимые импорты


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Предполагается, что функции f1, f2, f3 будут реализованы в одну строку
# В реализации функции f4 может быть до 3 строк

@print_result
def f1(arg):
    return sorted(Unique([d['job-name'] for d in arg], ignore_case=True))


@print_result
def f2(arg):
    return list(filter(lambda x: x[:11] == 'программист', arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом python', arg))


@print_result
def f4(arg):
    return [pair[0]+', зарплата '+str(pair[1])+' руб.' for pair in zip(arg, list(gen_random(len(arg), 100000, 200000)))]


if __name__ == '__main__':
    path = 'data_light.json'

    # Необходимо в переменную path сохранить путь к файлу, который был передан при запуске сценария

    with open(path, "r", encoding='UTF8') as f:
        data = json.load(f)

    with cm_timer_1():
        f4(f3(f2(f1(data))))

