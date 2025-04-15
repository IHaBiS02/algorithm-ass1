from memory_profiler import profile
import numpy as np
import sys
from data_generator import generate_array, generate_list
from tqdm import tqdm
import time
import datetime
from sort_checker import is_sorted
import tracemalloc
use_np_domain = True

def merge_procedure(A,p,q,r):
    # print(p,q,r)
    n1 = q - p + 1
    n2 = r - q
    # print(A.dtype)
    L = np.empty(n1+1, dtype=A.dtype)
    R = np.empty(n2+1, dtype=A.dtype)
    # L = [0 for _ in range(n1+1)]
    # R = [0 for _ in range(n2+1)]

    L[0:n1] = A[p : q + 1]
    R[0:n2] = A[q + 1 : r + 1]
    
    L[n1] = np.iinfo(A.dtype).max
    R[n2] = np.iinfo(A.dtype).max
    # L[n1] = np.iinfo(np.int64).max
    # R[n2] = np.iinfo(np.int64).max
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
    # current, peak = tracemalloc.get_traced_memory()
    # print(f"현재 메모리 사용량: {current / (1024*1024):.3f} MB")
    # print(f"실행 중 최댓값(peak)  : {peak / (1024*1024):.3f} MB")
    # print(tracemalloc.is_tracing())
    return A



if __name__ == "__main__":
    size, type = sys.argv[1:] # get array size and type
    array = generate_array(int(size), type)
    tracemalloc.start()
    start_snapshot = tracemalloc.take_snapshot()
    start = time.time()
    result_array = merge_sort(array)
    end = time.time()
    end_snapshot = tracemalloc.take_snapshot()
    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)
    print(is_sorted(result_array))
    stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    # 누가 메모리를 많이 쓰는지 상위 10개 라인 출력
    for stat in stats[:10]:
        print(stat)
    
    # 현재 메모리 사용량, 피크 사용량 확인
    current, peak = tracemalloc.get_traced_memory()
    print(f"현재 메모리 사용량: {current / (1024*1024):.3f} MB")
    print(f"실행 중 최댓값(peak)  : {peak / (1024*1024):.3f} MB")