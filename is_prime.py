# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from operator import eq

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

from collections import Counter
from itertools import combinations
from collections import deque
import heapq
import math


def my_permute(item, n):
    if n == 1:
        return len(item)
    for i in range(len(item)):
        temp_item = item[0, i] + item[i + 1,]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution(10))


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    r = int(math.sqrt(n))
    f = 5
    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        f += 6

    return True