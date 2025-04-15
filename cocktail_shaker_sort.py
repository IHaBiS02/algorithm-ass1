from memory_profiler import profile
import numpy as np
import sys
from data_generator import generate_array, generate_list
from tqdm import tqdm
import time
import datetime
from sort_checker import is_sorted

def cocktail_shaker_sort(A):
    front = 0
    end = len(A)-1
    swapped = True

    while swapped:
        swapped = False
        for i in range(front, end):
            if A[i] > A[i+1]:
                A[i],A[i+1]=A[i+1],A[i]
                swapped=True
        if not swapped:
            break
        end -= 1
        swapped=False
        for i in range(end,front,-1):
            if A[i] < A[i-1]:
                A[i],A[i-1]=A[i-1],A[i]
                swapped=True
        if not swapped:
            break
        front += 1
    return A





if __name__ == "__main__":
    size, type = sys.argv[1:] # get array size and type
    array = generate_array(int(size), type)
    start = time.time()
    result_array = cocktail_shaker_sort(array)
    end = time.time()
    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)
    print(is_sorted(result_array))
    # print(result_array)
    # insertion_sort(generate_list(int(size), type))