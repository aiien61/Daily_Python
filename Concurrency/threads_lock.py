from threading import Lock, Thread

task_lock: Lock = Lock()

def task(name: str):
    global task_lock
    for _ in range(3):
       # use lock to atomise the procedure line 10 to line 13
       task_lock.acquire()
       print(f"{name} - step 1\n", end='')
       print(f"{name} - step 2\n", end='')
       print(f"{name} - step 3\n", end='')
       task_lock.release()

t1: Thread = Thread(target=task, args=("Thread 1",))
t2: Thread = Thread(target=task, args=("Thread 2",))
t3: Thread = Thread(target=task, args=("Thread 3",))

t1.start()
t2.start()
t3.start()