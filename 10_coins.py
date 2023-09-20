"""
Задача 10:
На столе лежат n монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""

import random
import time
from typing import Union


def count_coins(*coins: Union[bool, int]) -> int:
    return min(map(lambda x: coins.count(x), (True, False)))


def count_coins_for(*coins: Union[bool, int]) -> int:
    counter1, counter2 = 0, 0
    for i in coins:
        if i:
            counter1 += 1
        else:
            counter2 += 1
    return counter1 if counter1 <= counter2 else counter2


def test_count_coins():
    while True:
        args = tuple(map(lambda _: random.random() > .5, range(random.randint(0, 1000))))
        print("PASS" if count_coins(*args) == count_coins_for(*args) else "FAILED")
        time.sleep(.1)


if __name__ == '__main__':
    test_count_coins()
