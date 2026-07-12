from multiprocessing import Pool

def sum_of_squares(n):
    """Calculate the sum of squares from 1 to n using mathematical formula."""
    return n * (n + 1) * (2 * n + 1) // 6

if __name__ == '__main__':
    inputs = [1000000, 2000000, 3000000, 4000000]
    
    # Pool() defaults to the number of available CPU cores
    with Pool() as pool:
        results = pool.map(sum_of_squares, inputs)
        
    print(results)