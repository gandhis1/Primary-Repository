""" 
Includes various test scripts used for testing Python libraries, 
statistical datasets, or IDE features.
"""
from random import randrange
from timeit import timeit

import numpy as np
import pandas as pd
from numba import jit

from typing import List


@jit(nopython=True)
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

@jit(nopython=True)
def quick_sort(raw_list):
    def quick_sort_recursive(raw_list, start, end):
        if start < end:
            partition = int(raw_list / 2)
            quick_sort_recursive()
            quick_sort_recursive()  
    pass # TODO - implement quick-sort

# TODO - test concurrent futures and asyncIO

rand_list = [randrange(0, 5000) for i in range(0, 5000)]
t_bubble_sort = timeit(stmt="bubble_sort(rand_list)",
                        setup="from __main__ import bubble_sort, rand_list",
                        number=1000)
t_python_sort = timeit(stmt="sorted(rand_list)",
                        setup="from __main__ import rand_list",
                        number=1000)
print("Python sort: {0}".format(t_python_sort))
print("{0} {1} ({2}x {3})".format("Bubble sort: ",
                                    t_bubble_sort,
                                    round(t_bubble_sort / t_python_sort, 1)),
                                    "slower")
sorting_equivalence = (bubble_sort(rand_list) == sorted(rand_list))
print("Equivalent: {}".format(str(sorting_equivalence)))
