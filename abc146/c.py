import os

def main():
	a,b,x = map(int, input().split())
	maxValue = 10**9 + 1
	minValue = 0

	while (maxValue - minValue) > 1:
		meanValue = (maxValue + minValue)//2
		y = a * meanValue + b * len(str(meanValue))
		if y > x:
			maxValue = meanValue
		else:
			minValue = meanValue
	print(minValue)

if __name__ == "__main__":
	main()
