import threading

def Even():
    print("First 10 Even Numbers:")
    for i in range(2, 21, 2):
        print(i)

def Odd():
    print("First 10 Odd Numbers:")
    for i in range(1, 20, 2):
        print(i)

def main():
    EThread = threading.Thread(target=Even)
    OThread = threading.Thread(target=Odd)

    EThread.start()
    OThread.start()

    EThread.join()
    OThread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()