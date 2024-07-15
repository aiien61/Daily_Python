import time
from threading import Thread

class MyThread(Thread):
    def __init__(self, thread_id: str, count: int):
        super().__init__()
        self.setName(thread_id)
        self.count: int = count


    def run(self) -> None:
        for i in range(10):
            print(f"Thread: {self.getName()} - {i}\n", end='')
            time.sleep(0.01)


def main():
    t1 = MyThread('1001', 10)
    t2 = MyThread('1002', 20)

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()