import functools

def planecoords():
	coords = (0, 0)
	moves = dict()
	moves['up'] 	= lambda x, a: (x[0]+abs(a), x[1])
	moves['down'] 	= lambda x, a: (x[0]-abs(a), x[1])
	moves['left'] 	= lambda x, a: (x[0], x[1]-abs(a))
	moves['right'] = lambda x, a: (x[0], x[1]+abs(a))
	
	while True:
		move = input('move: ').lower().split(' ')
		if len(move)>1:
			coords = moves[move[0]](coords, int(move[1]))
			print(move, coords)
		else:
			return(coords)		

def sortcountwords(words):
	return sorted([(i, words.count(i)) for i in set(words)])

def square(x):
	'''
	Return the square value of the input number.
	The input number must be integer.
	'''
	return x**2

class Person:
	def __init__(self, name):
		self.name = name

def tostring(n):
	return str(n)

def sumstrings(nums):
	s = lambda x,y: x+y
	return functools.reduce(s, [int(i) for i in nums])

def concatstring():
	sts = []
	while True:
		t = input('str: ')
		if t: sts.append(t)
		else: return ''.join(sts)

def maxstringlen():
	sts = []
	while True:
		t = input('sts: ')
		if t: sts.append((t, len(t)))
		else: break
	return [i[0] for i in sts if i[1]==max(sts, key=lambda x: x[1])[1]]

def isoddeven(num):
	return 'Num is odd' if num % 2 else 'Num is even'

if __name__ == '__main__':
	#Ex21
	#print(planecoords())
	
	#Ex22
	#print(*sortcountwords(input('txt: ').split(' ')), sep='\n')
	
	#Ex23
	#print(square(8), square(10))
	
	#Ex24
	#print(square.__doc__)
	
	#Ex25
	#jeff, knot = Person('Jeff'), Person('Knot')
	#print(jeff.name, knot.name, sep=', ')
	
	#Ex26
	#print(tostring(int(input('num: '))))

	#Ex27
	#print(sumstrings(input('nums: ').split(',')))
	
	#Ex28
	#print(concatstring())

	#Ex29
	#print(*maxstringlen(), sep='\n')

	#Ex30
	#print(isoddeven(int(input('num: '))))
