import re, functools

def trycatchdivby0():
	try:
		x = 5 / 0
	except ZeroDivisionError:
		print('Division by zero!')

def splitmail(mail):
	return (mail[:mail.index('@')], mail[mail.index('@')+1:mail.index('.')])

def getdigitonly(txt):
	return [re.findall('[0-9]+', txt)]

def specialchain(n):
	return functools.reduce(lambda x,y: x+y, list(map(lambda x: x/(x+1), range(1, n+1))))

def computerecursion(n):
	return 0 if not n else computerecursion(n-1)+100

def fib(n):
	return 1 if not n or n==1 else fib(n-1) + fib(n-2)
	
if __name__ == '__main__':
	#Ex51
	#raise(RuntimeError('Something went wrong'))
	#raise(StopIteration)

	#Ex52
	#trycatchdivby0()

	#Ex53
	#print(*splitmail('thisisuser@google.com'), sep='\n')

	#Ex54
	#print(*getdigitonly('2 cats and 3 dogs.'), sep=', ')

	#Ex55
	#print(u'hello world')

	#Ex57
	'''
	# -*- coding: utf-8 -*-
	'''
	
	#Ex58
	#print('{0:.2f}'.format(specialchain(5)))

	#Ex59
	#print(computerecursion(5))

	#Ex60
	#print([fib(i) for i in range(7)], sep=',')
