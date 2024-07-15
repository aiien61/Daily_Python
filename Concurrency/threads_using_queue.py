"""
Using Queue

queue.put(item, block=True/False, timeout=int)
    block: if True, the thread can't proceed if queue is full until queue is not full
    timeout: time in seconds to wait if queue is full, then forcefully proceed

queue.get(block=True/False, timeout=int)
    block: if True, the thread can't proceed if queue is empty until queue is not empty
    timeout: time in seconds to wait if queue is empty, then forcefully proceed

queue.qsize(): return the size of the queue

queue.empty(): check if the queue is empty

queue.full(): check if the queue is full

"""

from queue import Queue
from threading import Thread
from typing import List

class Producer(Thread):
    """Item Producer
    """
    def __init__(self, name: str, count: int, queue: Queue):
        super().__init__()
        self.setName(name)
        self.count: int = count
        self.queue: Queue = queue

    def run(self) -> None:
        for i in range(self.count):
            item: str = f"Item {i} -- produced by {self.getName()}"
            self.queue.put(item, block=True)


class Consumer(Thread):
    """Item Consumer
    """
    def __init__(self, name: str, queue: Queue):
        super().__init__()
        self.setName(name)
        self.setDaemon(True)  # if no items available, consumers will auto terminate 
        self.queue: Queue = queue

    def run(self) -> None:
        while True:
            item: str = self.queue.get(block=True)
            print(f"Item {item} consumed by {self.getName()}\n", end='')


def main():
    queue: Queue = Queue(3)
    threads: List[Thread] = []
    threads.append(Producer('Producer1', 10, queue))
    threads.append(Producer('Producer2', 10, queue))
    threads.append(Consumer('Consumer1', queue))
    threads.append(Consumer('Consumer2', queue))

    for t in threads:
        t.start()

if __name__ == "__main__":
    main()
