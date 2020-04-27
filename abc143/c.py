import os

def main():
	n = int(input())
	s = input()
	print(len(s))
	count = 1
	erser_count = 0
	for i in s:
		if count == len(s):
			break
		if i == s[count]:
			erser_count += 1
		count += 1
	print(n - erser_count)

if __name__ == "__main__":
	main()
