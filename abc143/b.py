import os

def main():
	n = int(input())
	d_list = list(map(int, input().split()))
	score = 0
	for i in range(n-1):
		for j in range(i+1,n):
			if len(d_list) == i:
				continue
			score += d_list[i] * d_list[j]
	print(score)

if __name__ == "__main__":
	main()
