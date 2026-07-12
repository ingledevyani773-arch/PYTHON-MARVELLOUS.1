import os
from multiprocessing import Pool

def count_evens(n):
    """Worker function to count even numbers up to N and get the process ID."""
    process_id = os.getpid()
    even_count = n // 2
    
    print(f"Process ID: {process_id}")
    print(f"Input Number: {n} Even Number Count: {even_count}\n")
    
    return even_count

if __name__ == '__main__':
    data_list = [1000000, 2000000, 3000000, 4000000]

    with Pool() as pool:

        pool.map(count_evens, data_list)