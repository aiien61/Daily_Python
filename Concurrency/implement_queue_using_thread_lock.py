from threading import Lock, Thread, Condition
from typing import List, Any

class SafeQueue:
    def __init__(self, size: int):
        self._item_list: List[Any] = []
        self.size: int = size
        self._item_lock: Lock = Condition()

    def put(self, item: Any) -> None:
        with self._item_lock:
            while len(self._item_list) >= self.size:
                self._item_lock.wait()

            self._item_list.append(item)
            self._item_lock.notify_all()

    def get(self) -> Any:
        with self._item_lock:
            while len(self._item_list) == 0:
                self._item_lock.wait()

            result = self._item_list.pop(0)
            self._item_lock.notify_all()
            return result


class Producer(Thread):
    """Item Producer
    """

    def __init__(self, name: str, count: int, queue: SafeQueue):
        super().__init__()
        self.name: str = name
        self.count: int = count
        self.queue: SafeQueue = queue

    def run(self) -> None:
        for i in range(self.count):
            item: str = f"Item {i} -- produced by {self.name}"
            self.queue.put(item)


class Consumer(Thread):
    """Item Consumer
    """

    def __init__(self, name: str, queue: SafeQueue):
        super().__init__()
        self.name: str = name
        # if no items available, consumers will auto terminate
        self.daemon: bool = True
        self.queue: SafeQueue = queue

    def run(self) -> None:
        while True:
            item: str = self.queue.get()
            print(f"Item {item} consumed by {self.name}\n", end='')


def main():
    queue: SafeQueue = SafeQueue(3)
    threads: List[Thread] = []
    threads.append(Producer('Producer1', 10, queue))
    threads.append(Producer('Producer2', 10, queue))
    threads.append(Consumer('Consumer1', queue))
    threads.append(Consumer('Consumer2', queue))

    for t in threads:
        t.start()


if __name__ == "__main__":
    main()
