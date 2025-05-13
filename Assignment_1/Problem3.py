def Add(no1,no2):
    no3 = 0
    no3 = no1 + no2
    return no3

def main():
    print("Enter first number")
    no1 = int(input())

    print("Enter Second number")
    no2 = int(input())

    ret = Add(no1,no2)

    print("Return value" , ret)

if __name__ == "__main__":
    main()


