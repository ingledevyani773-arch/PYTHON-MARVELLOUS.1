from multiprocessing import Pool
import math
import os

def calculate_factorial(n):
    """Calculates the factorial and retrieves the worker Process ID."""
    pid = os.getpid()
    result = math.factorial(n)
    return pid, n, result

if __name__ == '__main__':
    numbers = [10, 15, 20, 25]
    
    with Pool() as pool:

        results = pool.map(calculate_factorial, numbers)
        

    print(f"{'Process ID':<12} | {'Input Number':<12} | {'Factorial'}")
    print("-" * 45)
    for pid, num, fact in results:
        print(f"{pid:<12} | {num:<12} | {fact}")