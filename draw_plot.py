import os
import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot_folder_data(folder_path):
    random_time_path = os.path.join(folder_path, f"{folder}_random_time.csv")
    ascending_time_path = os.path.join(folder_path, f"{folder}_ascending_time.csv")
    descending_time_path = os.path.join(folder_path, f"{folder}_descending_time.csv")
    almost_sorted_time_path = os.path.join(folder_path, f"{folder}_almost_sorted_time.csv")

    random_memory_path = os.path.join(folder_path, f"{folder}_random_memory.csv")
    ascending_memory_path = os.path.join(folder_path, f"{folder}_ascending_memory.csv")
    descending_memory_path = os.path.join(folder_path, f"{folder}_descending_memory.csv")
    almost_sorted_memory_path = os.path.join(folder_path, f"{folder}_almost_sorted_memory.csv")

    df_random_time = None
    df_ascending_time = None
    df_descending_time = None
    df_almost_sorted_time = None

    if os.path.isfile(random_time_path):
        df_random_time = pd.read_csv(random_time_path, header=None, names=["n", "type", "time"])
    if os.path.isfile(ascending_time_path):
        df_ascending_time = pd.read_csv(ascending_time_path, header=None, names=["n", "type", "time"])
    if os.path.isfile(descending_time_path):
        df_descending_time = pd.read_csv(descending_time_path, header=None, names=["n", "type", "time"])
    if os.path.isfile(almost_sorted_time_path):
        df_almost_sorted_time = pd.read_csv(almost_sorted_time_path, header=None, names=["n", "type", "time"])

    df_random_memory = None
    df_ascending_memory = None
    df_descending_memory = None
    df_almost_sorted_memory = None

    if os.path.isfile(random_memory_path):
        df_random_memory = pd.read_csv(random_memory_path, header=None, names=["n", "type", "memory"])
    if os.path.isfile(ascending_memory_path):
        df_ascending_memory = pd.read_csv(ascending_memory_path, header=None, names=["n", "type", "memory"])
    if os.path.isfile(descending_memory_path):
        df_descending_memory = pd.read_csv(descending_memory_path, header=None, names=["n", "type", "memory"])
    if os.path.isfile(almost_sorted_memory_path):
        df_almost_sorted_memory = pd.read_csv(almost_sorted_memory_path, header=None, names=["n", "type", "memory"])

    plt.figure()

    if df_random_time is not None:
        plt.plot(df_random_time["n"], df_random_time["time"],
                 label=f"Random ({df_random_time['type'].iloc[0]})")

    if df_ascending_time is not None:
        plt.plot(df_ascending_time["n"], df_ascending_time["time"],
                 label=f"Ascending ({df_ascending_time['type'].iloc[0]})")
        
    if df_descending_time is not None:
        plt.plot(df_descending_time["n"], df_descending_time["time"],
                 label=f"Descending ({df_descending_time['type'].iloc[0]})")

    if df_almost_sorted_time is not None:
        plt.plot(df_almost_sorted_time["n"], df_almost_sorted_time["time"],
                 label=f"Almost Sorted ({df_almost_sorted_time['type'].iloc[0]})")

    plt.xlabel("Input Size (n)")
    plt.ylabel("Time")
    plt.title(f"{folder} Time Comparison")
    plt.legend()
    plt.show()

    plt.figure()

    if df_random_memory is not None:
        plt.plot(df_random_memory["n"], df_random_memory["memory"],
                 label=f"Random ({df_random_memory['type'].iloc[0]})")

    if df_ascending_memory is not None:
        plt.plot(df_ascending_memory["n"], df_ascending_memory["memory"],
                 label=f"Ascending ({df_ascending_memory['type'].iloc[0]})")

    # descending_memory
    if df_descending_memory is not None:
        plt.plot(df_descending_memory["n"], df_descending_memory["memory"],
                 label=f"Descending ({df_descending_memory['type'].iloc[0]})")

    # almost_sorted_memory
    if df_almost_sorted_memory is not None:
        plt.plot(df_almost_sorted_memory["n"], df_almost_sorted_memory["memory"],
                 label=f"Almost Sorted ({df_almost_sorted_memory['type'].iloc[0]})")

    plt.xlabel("Input Size (n)")
    plt.ylabel("Memory Usage")
    plt.title(f"{folder} Memory Comparison")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    folder = input("CSV 폴더 경로를 입력하세요: ")
    plot_folder_data(folder)
