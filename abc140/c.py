import os

def main():
	n = int(input())
	b_list = list(map(int, input().split()))
	result_list = [b_list[0]]*2
	for i in range(len(b_list)):
		if b_list[i] >= max(result_list[i],result_list[i+1]):
			pass
		else:
			result_list[i] = b_list[i]
		if i < len(b_list) - 1: 
			result_list.append(b_list[i+1])
	print(sum(result_list))

if __name__ == "__main__":
	main()
