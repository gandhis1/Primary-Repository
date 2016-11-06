#%%
import numpy as np
import pandas as pd
import sys
import numpy
from random import randrange
from timeit import timeit
from numba import jit

#%%
@jit(nopython=True)
def bubble_sort(raw_list):
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

#%%
@jit(nopython=True)
def quick_sort(raw_list):
    def quick_sort_recursive(raw_list, start, end):
        if start < end:
            partition = int(raw_list / 2)
            quick_sort_recursive()
            quick_sort_recursive()  
    pass # TODO - implement quick-sort

# TODO - test concurrent futures and asyncIO

#%%
random_list = [randrange(0, 5000) for i in range(0, 5000)]
time_bubble_sort = timeit(stmt="bubble_sort(random_list)",
                          setup="from __main__ import bubble_sort, random_list",
                          number=1000)
time_python_sort = timeit(stmt="sorted(random_list)",
                          setup="from __main__ import random_list",
                          number=1000)
print("Python sort: {0}".format(time_python_sort))
print("Bubble sort: {0} ({1}x slower)".format(time_bubble_sort,
                                              round(time_bubble_sort / time_python_sort, 1)))
print("Sorting equivalence: {}".format(str(bubble_sort(random_list) == sorted(random_list))))

#%% Weather manipulation
import calendar
import pandas as pd

noaa_stations = {"NEW YORK CNTRL PK TWR" : "USW00094728",
                 "CHICAGO UNIV" : "USW00014892"}

# Get weather data, limit to Chicago University and New York Central Park Tower stations
noaa_weather_data = r'ftp://ftp.ncdc.noaa.gov/pub/data/normals/1981-2010/products/temperature/dly-tavg-normal.txt'
weather_data = pd.read_csv(noaa_weather_data, delim_whitespace=True, header=None)
weather_data.columns = ["STATION", "MONTH"] + list(range(1, len(weather_data.columns) - 1))
weather_data = (weather_data
                    .loc[weather_data["STATION"].isin(noaa_stations.values())]
                    .reset_index(drop=True)
                    .set_index(["STATION", "MONTH"])
                    .rename_axis("DAY", axis=1)
                    .stack()
                    .reset_index()
                    .assign(MONTH = lambda x: list(map(lambda y: calendar.month_name[y], x["MONTH"]))))

%matplotlib inline
test = weather_data["DAY"].plot()
