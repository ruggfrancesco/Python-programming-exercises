import itertools

def sentences():
	a, b, c = ["I", "You"], ["Play", "Love"], ["Hockey","Football"]
	return [(i,j,k) for i in a for j in b for k in c]

def onlyoddnum(lst):
	return [i for i in lst if i % 2]

def remove5and7divs(lst):
	return [i for i in lst if not i%5 and not i%7]

def removenumsatind(lst):
	for i in range(0, len(lst), 2):
		lst[i] = False
	return filter(lambda x: x, lst)

def remove045(lst):
	a = [lst[0], lst[4], lst[5]]
	for i in a:
		lst.remove(i)
	return lst

def removeall24(lst):
	while(24 in lst):
		lst.remove(24)
	return lst

def intersect(lst1, lst2):
	return set([x for x in lst1 if x in lst2])

def sortedset(lst):
	ret = []
	for i in lst:
		if not i in ret:
			ret.append(i)
	return ret

class Person:
	def __init__(self):
		pass

class Male(Person):
	def __init__(self):
		self.gender = 'Male'
	def getGender(self):
		return self.gender

class Female(Person):
	def __init__(self):
		self.gender = 'Female'
	def getGender(self):
		return self.gender

def getlettercount(txt):
	return [(i, txt.count(i)) for i in sorted(set(txt))]

def chinesepuzzle(heads, legs):
	chicken = (legs - 2*heads)/2
	legs = legs/2
	return chicken, legs
	'''
		x + y = heads
		2x + 4y = legs
		
		x = heads - y
		
		2*heads - 2y + 4y = legs
		
		2y = legs - 2heads
		
			y = (legs - 2heads)/2 !!!
		
		x + (legs -2heads)/2 = heads
		
		x = legs/2
	'''
	

if __name__ == '__main__':
	#Ex71
	#print(*sentences(), sep='\n')

	#Ex72
	#print(*onlyoddnum([5,6,77,45,22,12,24]), sep=', ')

	#Ex73
	#print(*remove5and7divs([12,24,35,70,88,120,155]), sep=', ')

	#Ex74
	#print(*removenumsatind([12,24,35,70,88,120,155]), sep=', ')

	#Ex75
	#print(*[[[0 for i in range(0,3)] for j in range(0,5)] for k in range(0,8)], sep='\n')

	#Ex76
	#print(*remove045([12,24,35,70,88,120,155]), sep=', ')

	#Ex77
	#print(*removeall24([12,24,35,24,88,120,155]), sep=', ')

	#Ex78
	#print(intersect([1,3,6,78,35,55], [12,24,35,24,88,120,155]))

	#Ex79
	#print(sortedset([12,24,35,24,88,120,155,88,120,155]))

	#Ex80
	#jack, britney = Male(), Female()
	#print(jack.getGender(), britney.getGender())

	#Ex81
	#print(*getlettercount(input('txt: ')), sep='\n')

	#Ex82
	#print(''.join(reversed(input('txt: '))))

	#Ex83
	#print(input('txt: ')[::2])

	#Ex84
	#print(list(itertools.permutations([1,2,3])))

	#Ex85
	print(*chinesepuzzle(35, 94), sep=', ')
