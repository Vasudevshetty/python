"""
Real-world use case
Scenario: Web Scraing
Web Scraping often invloves making numerous network requests to ftch web pages.
Theses tasks are IO- bound they spend o a lot of time waiting for responses from servers.
Multithreading can significantly imporve the performance by allowing multiple web pages to be fetched concurrently
"""

import threading
import requests
from bs4 import BeautifulSoup
import multiprocessing
import math
import sys
import time

urls = [
    "https://python.langchain.com/v0.2/docs/introduction",
    "https://python.langchain.com/v0.2/docs/concepts",
    "https://python.langchain.com/v0.2/docs/tutorials",
]


def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    print(f"fetched {len(soup.text)} characters from {url}")


threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()


"""
Multiprocessing
scence: Fact calc
Fact calc, especially for large no, 
involove sign computation and can benefit from parallel processing.
"""

sys.set_int_max_str_digits(100000)


def fact(number):
    print(f"Computing factorial of {number}")
    result = math.factorial(number)
    print(f"Factorail of {number} is {result}")
    return result


if __name__ == "__main__":
    numbers = [5000, 6000, 700, 8000]

    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(fact, numbers)

    end_time = time.time() - start_time

    print(f"Results: {results}")
    print(f"Time taken: {end_time:.2f} seconds")
