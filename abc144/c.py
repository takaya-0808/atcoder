import os

def main():
	n = int(input())
	list_a = make_divisors(n)
	min_num = 1000000000000
	for i in range(0,len(list_a),2):
		if n//list_a[i] == list_a[i]:
			min_num = list_a[i] * 2 - 2
			break
		if min_num < (list_a[i] + list_a[i+1] - 2):
			pass
		else:
			min_num = list_a[i] + list_a[i+1] - 2
	print(min_num)
	
			


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    return divisors

	
if __name__ == "__main__":
	main()
