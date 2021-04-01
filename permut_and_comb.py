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
    ret = []
    if n == 1:
        for x in item:
            ret.append([x])
    else:
        for i in range(len(item)):
            tl = [item[i]]
            temp_item = item[0: i] + (item[i + 1:])
            temp_item = my_permute(temp_item, n - 1)
            for y in temp_item:
                ret.append(tl + y)
    return ret


def my_comb(item, n):
    ret = []
    if n == 1:
        for x in item:
            ret.append([x])
    else:
        for i in range(len(item)):
            tl = [item[i]]
            temp_item = my_comb(item[i+1:], n-1)
            for y in temp_item:
                ret.append(tl+y)
    return ret


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(my_permute(a, 3))
    print(my_comb(a, 3))
