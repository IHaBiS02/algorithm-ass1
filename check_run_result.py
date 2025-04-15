# this file has a function which check the memory usage and time consumed
# I really hope so, but who knows the future? Maybe the only thing I can make
# can be just some shit code

# memory-profiler is GOD!!!!!
# Well, it is not that good than I expected...

import time
import datetime
use_np_domain = True
import tracemalloc
import matplotlib.pyplot as plt
import csv
import sys
import os
from tqdm import tqdm

from bubble_sort import bubble_sort
from cocktail_shaker_sort import cocktail_shaker_sort
from insertion_sort import insertion_sort
from comb_sort import comb_sort
from heap_sort import heap_sort
from intro_sort import intro_sort
from quick_sort import quick_sort 
from selection_sort import selection_sort
from tournament_sort import tournament_sort
from merge_sort import merge_sort

from data_generator import generate_array

def measure_running_time(func, *args):
    size, type = args
    array = generate_array(int(size), type)
    start_time = time.time()
    func(array)
    end_time = time.time()
    running_time = end_time - start_time
    return running_time

def measure_memory_usage(func, *args):
    size, type = args
    array = generate_array(int(size), type)
    tracemalloc.start()
    func(array)
    first_size, first_peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return first_peak

def get_execute_time(func, size_list, type, output_file=None):
    time_table = []
    num_trials = 3
    for size in tqdm(size_list):
        total_time = 0
        for _ in range(num_trials):
            total_time += measure_running_time(func, size, type)
        average_time = total_time / num_trials
        time_table.append([size, type, average_time])
    
    if output_file:
        with open(output_file + "_time.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(time_table)
    return time_table

def get_memory_usage(func, size_list, type, output_file=None):
    memory_table = []
    num_trials = 1
    for size in tqdm(size_list):
        total_memory = 0
        for _ in range(num_trials):
            total_memory += measure_memory_usage(func, size, type)
        average_time = total_memory / num_trials
        memory_table.append([size, type, average_time])
    
    if output_file:
        with open(output_file + "_memory.csv", 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(memory_table)
    return memory_table


if __name__ == "__main__":
    func, output_file, type = sys.argv[1:]
    # size_list = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000, 6500, 7000, 7500, 8000, 8500, 9000, 9500, 10000]
    size_list = [1000, 2500, 4000, 5000,8000, 10000]
    # type = "ascending"
    if not os.path.exists(output_file):
        os.mkdir(output_file)
    output_file = output_file + "\\" + output_file + "_" + type
    
    if func == "bubble_sort":
        get_execute_time(bubble_sort, size_list, type, output_file)
        get_memory_usage(bubble_sort, size_list, type, output_file)
    if func == "cocktail_shaker_sort":
        get_execute_time(cocktail_shaker_sort, size_list, type, output_file)
        get_memory_usage(cocktail_shaker_sort, size_list, type, output_file)
    if func == "insertion_sort":
        get_execute_time(insertion_sort, size_list, type, output_file)
        get_memory_usage(insertion_sort, size_list, type, output_file)
    if func == "comb_sort":
        get_execute_time(comb_sort, size_list, type, output_file)
        get_memory_usage(comb_sort, size_list, type, output_file)
    if func == "heap_sort":
        get_execute_time(heap_sort, size_list, type, output_file)
        get_memory_usage(heap_sort, size_list, type, output_file)
    if func == "intro_sort":
        get_execute_time(intro_sort, size_list, type, output_file)
        get_memory_usage(intro_sort, size_list, type, output_file)
    if func == "quick_sort":
        get_execute_time(quick_sort, size_list, type, output_file)
        get_memory_usage(quick_sort, size_list, type, output_file)
    if func == "selection_sort":
        get_execute_time(selection_sort, size_list, type, output_file)
        get_memory_usage(selection_sort, size_list, type, output_file)
    if func == "tournament_sort":
        get_execute_time(tournament_sort, size_list, type, output_file)
        get_memory_usage(tournament_sort, size_list, type, output_file)
    if func == "merge_sort":
        get_execute_time(merge_sort, size_list, type, output_file)
        get_memory_usage(merge_sort, size_list, type, output_file)
    