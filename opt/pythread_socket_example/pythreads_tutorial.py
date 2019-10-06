import time
import threading

class MyThread(threading.Thread):
    id = 0
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id
    def run(self) -> None:
        print("Thread-" + str(self.id))
        time.sleep(5)

thread1 = MyThread(1)
thread2 = MyThread(2)
thread3 = MyThread(3)

thread1.start()
thread2.start()
thread3.start()
thread1.join()
thread2.join()
thread3.join()
