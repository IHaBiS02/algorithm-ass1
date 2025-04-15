from memory_profiler import profile
import numpy as np
import sys
from data_generator import generate_array, generate_list
from tqdm import tqdm
import time
import datetime
from sort_checker import is_sorted


def comb_sort(A, shrink_factor=1.3):
    n = len(A)
    
    gap = n
    swapped = True
    
    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink_factor))
        swapped = False
        for i in range(n - gap):
            if A[i] > A[i + gap]:
                A[i], A[i + gap] = A[i + gap], A[i]
                swapped = True
    return A


if __name__ == "__main__":
    size, type = sys.argv[1:] # get array size and type
    array = generate_array(int(size), type)
    start = time.time()
    result_array = comb_sort(array)
    end = time.time()
    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)
    print(is_sorted(result_array))
    # print(result_array)
    # insertion_sort(generate_list(int(size), type))
