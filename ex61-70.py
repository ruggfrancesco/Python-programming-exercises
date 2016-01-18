import math, random

def ngen(mx):
	n = 0
	while(n < mx):
		yield(n)
		n += 2

def div7gen(mx):
	n = 0
	while(n < mx):
		if not n%7 and not n%5: yield(n)
		n += 1

def binarysearch(search, lst):
	bot, top, index = 0, len(lst)-1, -1
	while(top>=bot and index==-1):
		mid = int(math.floor((top+bot)/2.0))
		if lst[mid]==search:
			index = mid
		elif lst[mid]>search:
			top = mid-1
		else:
			bot = mid+1
	return index

def exectime():
	from timeit import Timer
	t = Timer("for i in range(100):1+1")
	return(t.timeit())

if __name__ == '__main__':
	#Ex61
	#nums = ngen(int(input('num: ')))
	#print(*[i for i in nums], sep=',')

	#Ex62
	#print(*[i for i in div7gen(500)], sep=', ')

	#Ex63
	#for i in [2,4,6,8,13]:
	#	assert not i%2, 'Not even number'
	#print('Ok :)')
	
	#Ex64
	#print(eval(input('expr: ')))

	#Ex65
	#print(binarysearch(7, range(1,10)))

	#Ex66
	#print(math.floor(random.random()*100))

	#Ex67
	#print(math.floor(random.random()*100-5))

	#Ex68
	#print([random.randint(100,201) for i in range(0,5)])

	#Ex69
	#print(exectime())

	#Ex70
	#lst = [3,6,7,8]
	#random.shuffle(lst)
	#print(lst)
