import threading

def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True


def Prime(Data):
    print("Prime numbers are :")
    for i in Data:
        if ChkPrime(i):
            print(i, end=" ")
    print()


def NonPrime(Data):
    print("Non Prime numbers are :")
    for i in Data:
        if not ChkPrime(i):
            print(i, end=" ")
    print()


def main():
    Arr = list(map(int, input("Enter elements : ").split()))

    T1 = threading.Thread(target=Prime, args=(Arr,))
    T2 = threading.Thread(target=NonPrime, args=(Arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()