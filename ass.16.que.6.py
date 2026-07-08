def CheckNum(No):
    if(No>0):
        print("number is positive")
    elif(No<0):
        print("number is negative")
    else:
        print("number is zero")

def main():
    No=int(input("enter number"))

    CheckNum(No)



if __name__ == "__main__":
    main()