from memory_profiler import profile
import numpy as np
import sys
from data_generator import generate_array, generate_list
from tqdm import tqdm
import time
import datetime
from sort_checker import is_sorted

def merge_procedure(A,p,q,r):
    # print(p,q,r)
    n1 = q - p + 1
    n2 = r - q
    # print(A.dtype)
    L = np.empty(n1+1, dtype=A.dtype)
    R = np.empty(n2+1, dtype=A.dtype)

    L[0:n1] = A[p : q + 1]
    R[0:n2] = A[q + 1 : r + 1]
    
    L[n1] = np.iinfo(A.dtype).max
    R[n2] = np.iinfo(A.dtype).max

    i = 0
    j = 0
    for k in range(p,r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
    
    return A

def merge_sort(A,p=None,r=None):
    # print(A.dtype)
    if p == None and r == None:
        p = 0
        r = len(A)-1
    if p < r:
        q = (p+r)//2
        # print(A.dtype)
        merge_sort(A,p,q)
        # print(A.dtype)
        merge_sort(A,q+1,r)
        # print(A.dtype)
        merge_procedure(A,p,q,r)
    return A



if __name__ == "__main__":
    size, type = sys.argv[1:] # get array size and type
    start = time.time()
    result_array = merge_sort(generate_array(int(size), type))
    end = time.time()
    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)
    print(is_sorted(result_array))
    # print(result_array)

    # insertion_sort(generate_list(int(size), type))