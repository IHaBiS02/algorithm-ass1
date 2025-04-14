from memory_profiler import profile
import numpy as np
import sys
from data_generator import generate_array, generate_list
from tqdm import tqdm
import time
import datetime
from sort_checker import is_sorted

def partition (A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def quick_sort(A, p=None, r=None):
    if p == None and r == None: # set initial value
        p = 0
        r = len(A)-1
    if p < r:
        q = partition(A,p,r)
        quick_sort(A,p,q-1)
        quick_sort(A,q+1,r)
    return A



if __name__ == "__main__":
    size, type = sys.argv[1:] # get array size and type
    start = time.time()
    result_array = quick_sort(generate_array(int(size), type))
    end = time.time()
    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)
    print(is_sorted(result_array))
    # print(result_array)
    # insertion_sort(generate_list(int(size), type))