import os
from multiprocessing import Pool


def calculate_even_sum(n):
    """Calculates the sum of all even numbers from 1 to N using the arithmetic progression formula."""
    count = n // 2

    even_sum = count * (count + 1)

    pid = os.getpid()

    result = (
        f"Process ID: {pid}\n"
        f"Input Number: {n}\n"
        f"Sum of Even Numbers: {even_sum}\n"
    )
    return result


if __name__ == "__main__":
    
    data = [1000000, 2000000, 3000000, 4000000]

    with Pool() as pool:
        # Map the function to the data list to run in parallel
        results = pool.map(calculate_even_sum, data)

    for res in results:
        print(res)