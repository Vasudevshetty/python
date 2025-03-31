from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time

def print_number(number):
    time.sleep(1)
    return f"Number: {number}"

numbers = [1, 2, 3, 4, 5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)

for result in results:
    print(result)

def square(number):
    time.sleep(1)
    return f"Square: {number * number}"

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square, numbers)

    for result in results:
        print(result)