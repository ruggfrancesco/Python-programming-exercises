def mult57():
	lst = []
	for i in range(2000,3201):
		if(i%5 and not i%7): lst.append(i)
	return lst

def fact(n):
	return 1 if n==0 else n*fact(n-1)

def dictgen(mx):
	d = dict()
	for i in range(1, mx+1):
		d[i] = i*i
	return d

def genlistuple(nums):
	nums = [int(i) for i in nums.split(',')]
	return nums, tuple(nums)

class InputOutputString:
	def __init__(self, s=''):
		self.str = s
	def getString(self):
		self.str = input('str: ')
		return
	def printString(self):
		return self.str.upper()

if __name__=='__main__':
	#Ex1
	#print(*mult57(), sep=',')
	
	#Ex2
	#print(fact(int(input('fact: '))))
	
	#Ex3
	#print(dictgen(8))
	
	#Ex4
	#print(*genlistuple(input('nums: ')), sep='\n')
	
	#Ex5
	#st = InputOutputString('ciao')
	#print(st.printString())
	#st.getString()
	#print(st.printString())
