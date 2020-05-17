import os

def main():
    k = int(input())
    s = input()
    ans = ""
    if (len(s) <= k):
        print(s)
    else:
        ans = s[:k] + "..."
        print(ans)

if __name__ == "__main__":
    main()