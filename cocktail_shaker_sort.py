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
    array = generate_list(int(size), type)
    tracemalloc.start()
    start_snapshot = tracemalloc.take_snapshot()
    start = time.time()
    result_array = cocktail_shaker_sort(array)
    end = time.time()
    end_snapshot = tracemalloc.take_snapshot()
    sec = (end - start)
    result = datetime.timedelta(seconds=sec)
    print(result)
    print(is_sorted(result_array))
    stats = end_snapshot.compare_to(start_snapshot, 'lineno')
    # 누가 메모리를 많이 쓰는지 상위 10개 라인 출력
    # for stat in stats[:10]:
    #     print(stat)
    
    # 현재 메모리 사용량, 피크 사용량 확인
    current, peak = tracemalloc.get_traced_memory()
    print(f"현재 메모리 사용량: {current / (1024*1024):.3f} MB")
    print(f"실행 중 최댓값(peak)  : {peak / (1024*1024):.3f} MB")