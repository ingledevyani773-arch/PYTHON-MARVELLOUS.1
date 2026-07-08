import threading

def EvenFactor(No):
    Sum = 0

    print("Even Factors are:")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 == 0:
            print(i)
            Sum = Sum + i

    print("Sum of Even Factors:", Sum)


def OddFactor(No):
    Sum = 0

    print("Odd Factors are:")
    for i in range(1, No + 1):
        if No % i == 0 and i % 2 != 0:
            print(i)
            Sum = Sum + i

    print("Sum of Odd Factors:", Sum)


def main():
    Value = int(input("Enter number: "))

    EThread = threading.Thread(target=EvenFactor, args=(Value,))
    OThread = threading.Thread(target=OddFactor, args=(Value,))

    EThread.start()
    OThread.start()

    EThread.join()
    OThread.join()

    print("Exit from main")


if __name__ == "__main__":
    main()