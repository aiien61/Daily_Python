from threading import Thread


def multithreads_without_arguments():
    def task():
        for i in range(10):
            print(i)

    thread1 = Thread(target=task)
    thread2 = Thread(target=task)
    
    thread1.start()  # activate thread 1
    thread2.start()  # activate thread 2
    
    thread1.join()  # wait until thread 1 finishes
    thread2.join()  # wait until thread 2 finishes
    
    print("Main thread ends!")  # if thread 1 and 2 not finished, this line will not be executed


def multithreads_with_arguments():
    def task(count: int):
        for i in range(count):
            print(i)

    thread1 = Thread(target=task, args=(10,))
    thread2 = Thread(target=task, args=(20,))
    thread3 = Thread(target=task, args=(50,), daemon=True)  # daemon thread

    thread1.start()  # activate thread 1
    thread2.start()  # activate thread 2
    thread3.start()  # activate thread 3

    thread1.join()  # wait until thread 1 finishes
    thread2.join()  # wait until thread 2 finishes
    
    print("Main thread ends!")


if __name__ == "__main__":
    # multithreads_without_arguments()
    multithreads_with_arguments()