from memory_profiler import profile
import numpy as np
import sys
from data_generator import generate_array, generate_list
from tqdm import tqdm
import time
import datetime
from sort_checker import is_sorted

def max_heapify(A, i):
    L = i ** 2 # left index
    R = i ** 2 + 1 # right index

    largest = i

    if L <= A[0]:
        if A[L] > A[i]:
            largest = L
    
    if R <= A[0]:
        if A[R] > A[largest]:
            largest = R
    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A,largest)

def build_max_heap(A):
    A[0] = len(A)-1
    for i in range((len(A)-1)//2, 0, -1):
        max_heapify(A, i)

def heap_sort(A):
    heap_A = np.concatenate((np.array([0,]), A)) # heap_A[0] is value of heap size
    build_max_heap(heap_A)
    for i in range(len(heap_A)-1, 0, -1):
        heap_A[i], heap_A[1] = heap_A[1], heap_A[i]
        A[0] -= 1
        max_heapify(heap_A, 1)
    
    A = heap_A[1:]
    return A
        



if __name__ == "__main__":
    size, type = sys.argv[1:] # get array size and type
    array = generate_array(int(size), type)
    start = time.time()
    result_array = heap_sort(array)
    end = time.time()
    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)
    print(is_sorted(result_array))

    # insertion_sort(generate_list(int(size), type))