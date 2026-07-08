import threading

Counter = 0
LockObj = threading.Lock()


def Increment():
    global Counter

    for i in range(100000):
        LockObj.acquire()

        Counter = Counter + 1

        LockObj.release()


def main():
    T1 = threading.Thread(target=Increment)
    T2 = threading.Thread(target=Increment)
    T3 = threading.Thread(target=Increment)

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Final value of Counter :", Counter)


if __name__ == "__main__":
    main()