import multiprocessing
import time

def sum_of_fifth_powers(n):
    """Calculates 1^5 + 2^5 + ... + n^5"""
    total = 0
    for i in range(1, n + 1):
        total += i**5
    return total

def main():
    inputs = [1000000, 2000000, 3000000, 4000000]
    
    start_time = time.time()
    

    with multiprocessing.Pool() as pool:
        results = pool.map(sum_of_fifth_powers, inputs)
    

    end_time = time.time()
    
    print(f"Results: {results}")
    print(f"Total execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()