import pandas as pd
import dask.dataframe as dd

df = dd.read_csv('Data/20*.csv')


import functools

#decorators use a function but modifies it so that the function becomes something else

def my_decor(func):
    @functools.wraps(func)
    def function_runs_func():
        print('In the Decorator')
        func()
        print('After the decorator')
    #this line is v.imp. Here the modified function is returned.
    #so we pass in another function defined below and adds extra thing to it
    return function_runs_func()

#this function gets replaced by function_runs_func()
@my_decor
def my_func():
    print('I am the funciont!')

my_func()