"""
Includes various test scripts used for testing Python libraries,
statistical datasets, or IDE features.
"""
from random import randrange
from timeit import timeit
from itertools import groupby

from numba import jit

from typing import List, Tuple


def collapse_pp_string(pp: List[Tuple[int, float]]) -> List[Tuple[int, float]]:
    """
    Given a prepayment string, aggregate consecutive prepayment 
    provisions by adding their months if they have the same penalty.
    """
    return [(sum(map(lambda x: x[0], g)), key)
            for key, g in groupby(pp, lambda x: x[1])
            if key is not None]


@jit
def reverse_integer(x):
    """
    Given an integer x, returns the integer, reversed. 
    While one can do int(str(x)[::-1]), this implementation
    was chosen to use strictly numerical methods.
    """
    from math import ceil, log
    powers = list(range(1, ceil(log(x, 10)) + 1))
    new_number = 0
    for i, j in zip(powers, powers[::-1]):
        divisor = 10 ** i
        subtract = 10 ** (i - 1)
        multiplier = 10 ** (j - 1)
        new_number += ((x % divisor) // subtract) * multiplier
    return new_number


@jit
def largestPalindrome(n):
    """
    :type n: int
    :rtype: int
    """
    n_lower = int('1' + ''.join(['0'] * (n - 1)))
    n_upper = int(''.join(['9'] * n))
    prod_upper = n_upper ** 2
    for prod in reversed(range(0, prod_upper + 1)):
        if str(prod) == ''.join(reversed(str(prod))):
            for i in reversed(range(n_lower, n_upper + 1)):
                if prod % i == 0:
                    j = prod / i
                    if len(str(j)) == n:
                        return prod % 1337
                    else:
                        continue


@jit
def bubble_sort(raw_list: List[int]):
    for i in range(0, len(raw_list)):
        is_sorted = True
        for j in range(0, len(raw_list) - i - 1):
            a = raw_list[j]
            b = raw_list[j + 1]
            if a > b:
                is_sorted = False
                raw_list[j], raw_list[j + 1] = b, a
        if is_sorted:
            break
    return raw_list


def quick_sort(seq):
    if seq:  # if given list (or tuple) with one ordered item or more:
        pivot = seq[0]
        # below will be less than:
        below = [i for i in seq[1:] if i < pivot]
        # above will be greater than or equal to:
        above = [i for i in seq[1:] if i >= pivot]
        return quick_sort(below) + [pivot] + quick_sort(above)
    else:
        return seq  # empty list


def sorting_test():
    t_bubble_sort = timeit(stmt="bubble_sort(rand_list)",
                           setup="from __main__ import bubble_sort, rand_list",
                           number=100)
    t_quick_sort = timeit(stmt="quick_sort(rand_list)",
                          setup="from __main__ import quick_sort, rand_list",
                          number=100)
    t_python_sort = timeit(stmt="sorted(rand_list)",
                           setup="from __main__ import rand_list",
                           number=100)

    print("Python sort: {0}".format(t_python_sort))

    for sort_time, sort_name in zip([t_bubble_sort, t_quick_sort],
                                    ['Bubble Sort', 'Quick Sort']):
        print("{0} {1} ({2}x {3})".format(sort_name + ": ", sort_time,
                                          round(t_bubble_sort / sort_time, 1),
                                          "slower"))


rand_list = [randrange(0, 5000) for i in range(0, 5000)]


def main():
    pp = [(12, 0.02), (16, 0.02), (6, 0.015), 
          (12, 0.012), (6, 0.012), (36, 0.01)]
    print(collapse_pp_string(pp))


if __name__ == "__main__":
    main()
