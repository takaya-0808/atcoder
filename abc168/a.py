import os

def main():
    n = input()
    if(int(n[-1]) == 2): 
        print("hon")
    elif (int(n[-1]) == 4):
        print("hon")
    elif (int(n[-1]) == 5):
        print("hon")
    elif (int(n[-1]) == 7):
        print("hon")
    elif (int(n[-1]) == 9):
        print("hon")
    elif (int(n[-1]) == 0):
        print("pon")
    elif (int(n[-1]) == 1):
        print("pon")
    elif (int(n[-1]) == 6):
        print("pon")
    elif (int(n[-1]) == 8):
        print("pon")
    else:
        print("bon")

if __name__ == "__main__":
    main()