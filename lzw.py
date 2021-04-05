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
import string


def lzw(msg):
    answer = []
    my_dict = {}
    idx = 1
    for i in range(len(string.ascii_uppercase)):
        my_dict.update({string.ascii_uppercase[i]: idx})
        idx += 1
    out_idx = 0
    while out_idx < len(msg):
        temp = out_idx + 1
        if out_idx is len(msg)-1:
            answer.append(my_dict[msg[out_idx:temp]])
            break
        while my_dict.get(msg[out_idx:temp]) is not None:
            temp += 1
            if temp > len(msg):
                break
        temp -= 1

        answer.append(my_dict[msg[out_idx:temp]])
        my_dict.update({msg[out_idx:temp + 1]: idx})
        idx += 1
        out_idx += (temp-out_idx)
    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(lzw('asdf'))
