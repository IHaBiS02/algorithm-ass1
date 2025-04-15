from memory_profiler import profile
import numpy as np
import sys
from data_generator import generate_array, generate_list
from tqdm import tqdm
import time
import datetime
from sort_checker import is_sorted
from heap_sort import heap_sort
from insertion_sort import insertion_sort


def partition (A,p,r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def intro_sort(A, p=None, r=None, depth=0):
    if p == None and r == None: # set initial value
        p = 0
        r = len(A)-1
        if p < r:
            if len(A) <= 16:
                A[p:r+1] = insertion_sort(A[p:r+1])
            if depth > 2 * np.log2(len(A)):
                A[p:r+1] = heap_sort(A[p:r+1])
            else:
                q = partition(A,p,r)
                intro_sort(A,p,q-1,depth+1)
                intro_sort(A,q+1,r,depth+1)
        insertion_sort(A)
        return A
    else:
        if p < r:
            if len(A) <= 16:
                A[p:r+1] = insertion_sort(A[p:r+1])
            if depth > 2 * np.log2(len(A)):
                A[p:r+1] = heap_sort(A[p:r+1])
            else:
                q = partition(A,p,r)
                intro_sort(A,p,q-1,depth+1)
                intro_sort(A,q+1,r,depth+1)


if __name__ == "__main__":
    size, type = sys.argv[1:] # get array size and type
    array = generate_array(int(size), type)
    start = time.time()
    result_array = intro_sort(array)
    end = time.time()
    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)
    print(is_sorted(result_array))
    # print(result_array)
    # insertion_sort(generate_list(int(size), type))
