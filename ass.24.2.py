import os
from multiprocessing import Pool


def calculate_odd_sum(n):
    """Calculates the sum of odd numbers from 1 to N and prints the result."""
    num_of_odds = (n + 1) // 2
    total_sum = num_of_odds * num_of_odds

    print(f"Process ID: {os.getpid()}")
    print(f"Input Number: {n}")
    print(f"Sum of Odd Numbers: {total_sum}")
    print("-" * 30)  

    return total_sum


if __name__ == "__main__":
    
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as pool:
        # Map the function to the data across the pool
        pool.map(calculate_odd_sum, data)