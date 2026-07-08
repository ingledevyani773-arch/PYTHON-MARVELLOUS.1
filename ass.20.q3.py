import threading

def EvenList(Data):
    Sum = 0

    for i in Data:
        if i % 2 == 0:
            Sum = Sum + i

    print("Sum of even elements is :", Sum)


def OddList(Data):
    Sum = 0

    for i in Data:
        if i % 2 != 0:
            Sum = Sum + i

    print("Sum of odd elements is :", Sum)


def main():
    Arr = []

    Size = int(input("Enter number of elements : "))

    print("Enter the elements :")

    for i in range(Size):
        No = int(input())
        Arr.append(No)

    EThread = threading.Thread(target=EvenList, args=(Arr,))
    OThread = threading.Thread(target=OddList, args=(Arr,))

    EThread.start()
    OThread.start()

    EThread.join()
    OThread.join()

    print("Exit from main")


if __name__ == "__main__":
    main()