from threading import Thread, Lock
import time

tLock = Lock()


def timer(name, delay, repeat):
    print("Timer {} started.".format(name))
    tLock.acquire()
    print(name + " is acquired the lock.")
    while repeat > 0:
            time.sleep(delay)
            print(name + ":" + str(time.ctime(time.time())))
            repeat -= 1
    print(name + " is releasing the lock.")
    tLock.release()
    print("Timer {} completed.".format(name))


def Main():
    t1 = Thread(target=timer, args=("Timer1", 1, 5))
    t2 = Thread(target=timer, args=("Timer2", 2, 5))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("Main completed.")


if __name__ == '__main__':
    Main()
