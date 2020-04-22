import os

def main():
	s = input()
	seikai = 0
	s = list(s)
	for i,v in enumerate(s):
		if i == 2 or i == 4:
			if s[i] == s[i+1]:
				seikai += 1
	
	if seikai == 2:
		print("Yes")
	else:
		print("No")
			

if __name__ == "__main__":
	main()
