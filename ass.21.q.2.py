import threading

def Maximum(Data):
    print("Maximum element is :", max(Data))


def Minimum(Data):
    print("Minimum element is :", min(Data))


def main():
    Arr = list(map(int, input("Enter elements : ").split()))

    T1 = threading.Thread(target=Maximum, args=(Arr,))
    T2 = threading.Thread(target=Minimum, args=(Arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()