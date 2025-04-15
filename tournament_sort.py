from memory_profiler import profile
import numpy as np
import sys
from data_generator import generate_array, generate_list
from tqdm import tqdm
import time
import datetime
from sort_checker import is_sorted
import math

def build_tree(A):
    tree_size = 2**(math.ceil(math.log2(len(A)))+1)
    temp = np.full(tree_size+1, np.iinfo(A.dtype).max,dtype=A.dtype)
    for i in range(len(A)):
        temp[(tree_size//2) + i] = A[i]
    for i in range(tree_size//2-1, 0, -1):
        right = temp[i*2+1]
        left = temp[i*2]
        temp[i] = min(left, right)
    return temp

def tree_delete_value(tree, value):
    i = 1
    while i < len(tree):
        if tree[i] == value:
            tree[i] = np.iinfo(tree.dtype).max
            if tree[i * 2] == value:
                i = i * 2
            else:
                i = i * 2 + 1
        else:
            break
    return tree

def pop_tree(tree):
    min_val = tree[0]
    tree = tree_delete_value(tree, min_val)
    return min_val

def rebuild_tree(tree):
    for i in range(len(tree)//2-1, 0, -1):
        right = tree[i*2+1]
        left = tree[i*2]
        tree[i] = min(left, right)
    return tree
        
    
def tournament_sort(A):
    n = len(A)
    tree = build_tree(A)

    for i in range(n):
        min_val = pop_tree(tree)
        rebuild_tree(tree)
        A[i] = min_val
 
    return A


if __name__ == "__main__":
    size, type = sys.argv[1:] # get array size and type
    array = generate_array(int(size), type)
    start = time.time()
    result_array = tournament_sort(array)
    end = time.time()
    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)
    print(is_sorted(result_array))
    # print(result_array)
    # insertion_sort(generate_list(int(size), type))
