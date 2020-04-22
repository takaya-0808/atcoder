
def main():
	happy_count = 0
	money = int(input())
	happy_count = (money // 500) * 1000
	money -= (money//500) * 500
	happy_count += (money//5) * 5
	print(happy_count)
		

if __name__ == "__main__":
	main()
