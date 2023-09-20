"""
Задача 14:
Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числа N.
"""

import random
import time
from math import log2
from typing import List, Tuple


def pow_2(_n: int) -> List[Tuple[int, int]]:
    _ = [(0, 1), ]
    assert _n >= 0, f'{_n} != степень числа 2.'
    while _n >= _[-1][1]:
        _.append(
            (_[-1][0] + 1, _[-1][1] * 2)
        )
    return _[:-1]


def pow_2_lg(_n: int) -> List[Tuple[int, int]]:
    _ = []
    assert _n >= 0, f'{_n} != степень числа 2.'
    for i in range(int(log2(_n)) + 1):
        _.append(
            (i, 2 ** i)
        )
    return _


def test_pow_2():
    while True:
        n = random.randint(1, 1000)
        # print(n)
        pw, pw_lg = pow_2(n), pow_2_lg(n)
        # print('pow_2', pw)
        # print('pow_2_lg', pw_lg)
        print("PASS" if pw_lg == pw else "FAILED")
        time.sleep(.1)


if __name__ == '__main__':
    test_pow_2()
