# checking if array is sorted or not
import numpy as np

def is_sorted(A):
    if np.array_equal(A, np.sort(A)):
        return True
    return False
