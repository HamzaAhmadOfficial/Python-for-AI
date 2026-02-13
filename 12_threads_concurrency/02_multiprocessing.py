from multiprocessing import Process, process
from os import name
import time

def brew_chai(name):
    print(f"Start of {name} Chai brewing")
    time.sleep(3)
    print(f"End of {name} Chai brewing")

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
        for i in range(3)
    ]

    # Start all processes
    for p in chai_makers:
        p.start()

    # Wait for all to finish
    for p in chai_makers:
        p.join()