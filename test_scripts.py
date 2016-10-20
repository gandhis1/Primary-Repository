#%%
import numpy as np
import pandas as pd
import sys
import numpy
from random import randrange
from timeit import timeit
from numba import jit

#%%
@jit(nopython=True, )
def bubble_sort(list):
    for i in range(0, len(list)):
        is_sorted = True
        for j in range(0, len(list) - i - 1):
            a = list[j]
            b = list[j + 1]
            if a > b:
                is_sorted = False
                list[j], list[j + 1] = b, a
        if is_sorted:
            break
    return list 

#%%
random_list = [randrange(0, 5000) for i in range(0, 5000)]
time_bubble_sort = timeit(stmt="bubble_sort(random_list)",
                          setup="from __main__ import bubble_sort, random_list",
                          number=100)
time_python_sort = timeit(stmt="sorted(random_list)", 
                          setup="from __main__ import random_list",
                          number=100)
print("Bubble sort: {0}".format(time_bubble_sort))
print("Python sort: {0} ({1}x)".format(time_python_sort, 
                                       round(time_bubble_sort / time_python_sort, 1)))
print("Sorting equivalence: {}".format(str(bubble_sort(random_list) == sorted(random_list))))
