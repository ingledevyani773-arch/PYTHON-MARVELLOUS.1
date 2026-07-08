def Add(No1,NO2):
    Ans=No1+NO2
    return Ans
    

def main():
    No1= int(input("Enter No1:"))
    
    No2= int(input("Enter No2:"))
    Ret1=Add(No1,No2)
    print("Addition is :",Ret1)

if __name__ == "__main__":
    main()