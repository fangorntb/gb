"""
Задача 12:
Петя и Катя – брат и сестра.
Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать.
Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
"""

import random
import time
from typing import Optional, Tuple


def find_nums(_s: int, _pow: int) -> Optional[Tuple[int, int]]:
    for i in range(_s+1):
        for j in range(_s+1):
            if i + j < _s:
                continue
            elif i * j == _pow and i + j == _s:
                return i, j


def test_find_nums():
    for _ in range(100_000):
        a = random.randint(0, 1000)
        b = random.randint(0, 1000)
        s = a + b
        pw = a * b
        if tuple(sorted(find_nums(s, pw))) == tuple(sorted((a, b))):
            print('PASS')
        else:
            print(a, b, s, pw)
            print('FAILED')
        time.sleep(.1)



if __name__ == '__main__':
    test_find_nums()
