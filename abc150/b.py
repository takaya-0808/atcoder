import os

def main():
	count = 0
	num = int(input())
	strings = input()
	
	for i in range(0,num-3,1):
		if strings[i] == "A" and strings[i+1] == "B" and strings[i+2] == "C":	
			count += 1
	print(count)

if __name__ == '__main__':
	main()
