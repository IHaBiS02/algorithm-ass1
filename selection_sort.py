from memory_profiler import profile
import numpy as np
import sys
from data_generator import generate_array, generate_list
from tqdm import tqdm
import time
import datetime
from sort_checker import is_sorted

def selection_sort(A):
    for i in range(len(A)-1):
        min = np.iinfo(A.dtype).max
        min_index = None
        for j in range(i, len(A)):
            if A[j] < min:
                min = A[j]
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A


if __name__ == "__main__":
    size, type = sys.argv[1:] # get array size and type
    start = time.time()
    result_array = selection_sort(generate_array(int(size), type))
    end = time.time()
    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)
    print(is_sorted(result_array))
    # print(result_array)
    # insertion_sort(generate_list(int(size), type))