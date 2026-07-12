import os

def count_odd_numbers(n):
    return (n + 1) // 2

def main():
    process_id = os.getpid()
    data = [1000000, 2000000, 3000000, 4000000]
    
    for number in data:
        odd_count = count_odd_numbers(number)
        print(f"Process ID: {process_id} Input Number: {number:,}")
        print(f"Odd Number Count: {odd_count:,}\n")

if __name__ == "__main__":
    main()