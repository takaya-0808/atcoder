import os
from itertools import permutations

def main():
	p_score, q_score, count = 0,0,0
	string = ""
	num = int(input())
	p_num = tuple(list(map(str, input().split())))
	q_num = tuple(list(map(str, input().split())))
	for i in range(1,num+1):
		string  = string + str(i) 
	list_ = list(permutations(string, num))
	
	for i in list_:

		count += 1
		if p_num == i:
			q_score = count
		if q_num == i:
			p_score = count
	
		
	print(abs(q_score - p_score))
		


if __name__ == '__main__':
	main()
