import math

def formula(nums):
	C, H = 50, 30
	return [round(math.sqrt((2*C*int(i))/H)) for i in nums.split(',')]

def matrix(xy):
	return [[i*j for i in range(0,int(xy[1]))] for j in range(0, int(xy[0]))]

def sortwords(words):
	return sorted(words)

def capsmultipleline():
	lst = []
	while True:
		tmp = input()
		if tmp:
			lst.append(tmp.upper())
		else:
			return lst

def printsetsortword(words):
	return sorted(set(words))

if __name__ == '__main__':
	#Ex6
	#print(*formula(input('nums: ')), sep=',')
	
	#Ex7
	#print(*matrix(input('x,y: ').split(',')), sep='\n')
	
	#Ex8
	#print(*sortwords(input('words: ').split(',')), sep='\n')
	
	#Ex9
	#print(*capsmultipleline(), sep='\n')
	
	#Ex10
	print(*sorted(set(input('words: ').split(' '))), sep=' ')
