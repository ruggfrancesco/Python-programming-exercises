def printdict(n):
	d = dict()
	for i in range(1, n+1):
		d[i] = i**2
	return d

def powerlist(n):
	return [i**2 for i in range(1, n+1)]

def powertuple(n):
	return tuple([i**2 for i in range(1, n+1)])

def halfline(tup):
	return tup[:int(len(tup)/2)], tup[int(len(tup)/2):]

def numeven(tup):
	return tuple([i for i in tup if not i % 2])

def isyesok(y):
	return True if y.lower()=='yes' else False
	

if __name__ == '__main__':
	#Ex31
	#print(printdict(3))
	
	#Ex32
	#print(printdict(20))

	#Ex33
	#print(powerlist(20))

	#Ex34
	#print(powerlist(20)[:5])

	#Ex35
	#print(powerlist(20)[-5:])

	#Ex36
	#print(powerlist(20)[5:])

	#Ex37
	#print(powertuple(20))

	#Ex38
	#print(*halfline((1,2,3,4,5,6,7,8,9,10)), sep='\n')

	#Ex39
	#print(numeven((1,2,3,4,5,6,7,8,9,10)))

	#Ex40
	#print(isyesok('Yes'))
