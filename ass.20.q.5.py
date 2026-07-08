import threading

def DisplayForward():
    print("Thread1 Output:")
    for i in range(1, 51):
        print(i, end=" ")
    print()


def DisplayReverse():
    print("Thread2 Output:")
    for i in range(50, 0, -1):
        print(i, end=" ")
    print()


def main():
    T1 = threading.Thread(target=DisplayForward, name="Thread1")
    T2 = threading.Thread(target=DisplayReverse, name="Thread2")

    T1.start()

    # Wait for Thread1 to complete
    T1.join()

    # Start Thread2 only after Thread1 finishes
    T2.start()

    T2.join()

    print("Exit from main")


if __name__ == "__main__":
    main()