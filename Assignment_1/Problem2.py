def chkNum(no):
    if no % 2 == 0:
        return "Even Number"
    else:
        return "Odd Number"
def main():
    print("Please enter number")
    no = int (input())
    evenorodd = chkNum(no)
    print(evenorodd)

if __name__ == "__main__":
    main()
