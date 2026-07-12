import multiprocessing

def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes_up_to(n):
    """Counts how many prime numbers exist between 1 and n."""
    return sum(1 for i in range(1, n + 1) if is_prime(i))

if __name__ == "__main__":
    numbers = [10000, 20000, 30000, 40000]
    
    with multiprocessing.Pool() as pool:

        results = pool.map(count_primes_up_to, numbers)
    

    for num, count in zip(numbers, results):
        print(f"Total primes up to {num}: {count}")