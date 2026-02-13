from itertools import count
from multiprocessing import Process, process
import time

from networkx import prominent_group

def crunch_numbers():
    print(f"Started the count process...")
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process...")

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_numbers)
    p2 = Process(target=crunch_numbers)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time taken with multiprocessig is : {end - start} seconds")