import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, thread_id: str, count: int, is_daemon: bool = True):
        super().__init__()
        self.setName(thread_id)
        if is_daemon:
            self.setDaemon(True)
        self.count: int = count

    def run(self) -> None:
        for i in range(10):
            print(f"Thread: {self.getName()} - {i}\n", end='')
            time.sleep(0.01)


def main():
    t1 = MyThread('1001', 10, is_daemon=False)
    t2 = MyThread('1002', 50, is_daemon=True)  # set as daemon, then if t1 finishes, t2 will be terminated

    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
