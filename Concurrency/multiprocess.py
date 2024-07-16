import time
from multiprocessing import Process
from typing import List

def task(name: str, count: int) -> None:
    print(f"{name} - start\n", end='')
    result = 0
    for i in range(count):
        result += i

    time.sleep(1)
    print(f"{name} - end with {result}\n", end='')

def start_process() -> None:
    # Process will auto activate multi processes and distribute them to the task
    process: Process = Process(target=task, args=("A", 100))
    process.start()
    process.join()
    print("Main thread ends!")

def start_multiprocess() -> None:
    args_list: List[tuple] = [("A", 100), ("B", 200), ("C", 300)]
    processes: List[Process] = [Process(target=task, args=[name, count]) for name, count in args_list]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("Main thread ends!")


if __name__ == '__main__':
    # start_process()
    start_multiprocess()
