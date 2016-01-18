import re

def binmod5(nums):
	return [sts for sts in nums if(not int(sts, 2) % int('101',2))]

def numevendigits():
	def allevendigits(x):
		while(x > 0):
			if((x % 10) % 2): return False
			x = int(x/10)
		return True
	return [i for i in range(1000,3001) if(allevendigits(i))]

def findletterdigitnumbers(phrase):
	return (	'Letters: ' + str(len(''.join(re.findall('[A-Za-z]+', phrase)))),
				'Numbers: ' + str(len(''.join(re.findall('[0-9]+', phrase))))
			 )

def numupperlower(phrase):
	upp, low = 0, 0
	for l in phrase:
		if l.isupper(): upp += 1
		if l.islower(): low += 1
	return 'Upper: '+str(upp), 'Lower: '+str(low)

def squarelistifodd(nums):
	return [int(i)**2 for i in nums if(int(i)%2)]

def bankaccount():
	balance = 0
	while True:
		st = input('Operation: ')
		if st:
			if st[0] == 'D':
				balance += int(re.sub('[A-Za-z ]+', '', st))
			elif st[0] == 'W':
				balance -= int(re.sub('[A-Za-z ]+', '', st))
		else:
			return balance

def checkpassword(psw):
	rules = ['[a-z]', '[0-9]', '[A-Z]', '[$#@]']
	def isok(p):
		if(not 6<=len(p)<=12): return False
		for rule in rules:
			if not re.search(rule, p):
				return False
		return True
	return [p for p in psw if isok(p)]

def sortedlist():
	lst = []
	while True:
		s = input('row: ')
		if s:
			lst.append(s)
		else:
			break
	return sorted(lst, key = lambda x: (x[0], x[1], x[2]))

def sevengen(maximum):
	for num in range(0, maximum):
		if not num % 7:
			yield num

if __name__ == '__main__':
	#Ex11
	#print(*binmod5(input('nums: ').split(',')), sep=',')
	
	#Ex12
	#print(*numevendigits(), sep=',')
	
	#Ex13
	#print(*findletterdigitnumbers(input('txt: ')), sep='\n')
	
	#Ex14
	#print(*numupperlower(input('txt: ')), sep='\n')
	
	#Ex15
	#print(eval(re.sub('a', input('num: '), 'a+aa+aaa+aaaa')))
	
	#Ex16
	#print(*squarelistifodd(input('nums: ').split(',')), sep=',')
	
	#Ex17
	#print(bankaccount())

	#Ex18
	#print(*checkpassword(input('psw: ').split(',')), sep=',')
	
	#Ex19
	#print(*sortedlist(), sep='\n')
	
	#Ex20
	modseven = sevengen(100)
	print([i for i in modseven])
