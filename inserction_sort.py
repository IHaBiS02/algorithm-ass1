from memory_profiler import profile
import numpy as np
import sys
from data_generator import generate_array, generate_list
from tqdm import tqdm
import time
import datetime
from sort_checker import is_sorted

# @profile()
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

if __name__ == "__main__":
    size, type = sys.argv[1:] # get array size and type
    array = generate_array(int(size), type)
    start = time.time()
    result_array = insertion_sort(array)
    end = time.time()
    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)
    print(is_sorted(result_array))
    
    # insertion_sort(generate_list(int(size), type))