import math
import os
from multiprocessing import Pool

def calculate_factorial(n):
    """Calculates the factorial and gathers process and result details."""
    result = math.factorial(n)
    
    output = (
        f"Process ID: {os.getpid()}\n"
        f"Input Number: {n}\n"
        f"Factorial {result}\n"
    )
    return output

if __name__ == '__main__':
    data = [10, 15, 20, 25]
    
    with Pool() as pool:
        results = pool.map(calculate_factorial, data)
        
    for res in results:
        print(res)