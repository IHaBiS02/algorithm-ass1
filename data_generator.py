# it will generate many types of list through function

import numpy as np

def generate_array(size, type):
    if type == "ascending":
        return np.array(range(size))
    if type == "descending":
        return np.array(range(size-1, -1, -1))
    if type == "random":
        temp = np.array(range(size))
        temp = np.random.permutation(temp)
        # print(temp.dtype)
        return temp
    

def generate_list(size, type):
    if type == "ascending":
        return list(np.array(range(size)))
    if type == "descending":
        return list(np.array(range(size-1, -1, -1)))
    if type == "random":
        temp = np.array(range(size))
        np.random.shuffle(temp)
        return list(temp)
    