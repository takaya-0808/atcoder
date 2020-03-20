import os

def main():
	num = list(map(int, input().split()))	
	if num[0] == num[1] or num[0] == num[2]:
		if num[1] == num[2]:
			print("No")
		else:
			print("Yes")
	else:
		if num[1] == num[2]:
			print("Yes")
		else:
			print("No")

if __name__ == "__main__":
	main()