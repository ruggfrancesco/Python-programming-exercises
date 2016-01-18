import math

def filtereven(tup):
	return filter(lambda x: not x%2, tup)

def squaresof(tup):
	return map(lambda x: x**2, tup)

def squaresofeven(tup):
	return map(lambda p: p**2, filter(lambda x: not x%2, tup))

def filterevennum(n):
	return filter(lambda x: not x%2, range(1, n+1))

def mapsquares(lst):
	return map(lambda x: x**2, lst)

class American:
	def __init__(self):
		self.nationality = 'American'
	
	def printNationality(self):
		print(self.nationality)
		return

class NewYorker(American):
	pass

class Circle:
	def __init__(self, rad):
		self.rad = rad
	
	def area(self):
		return self.rad**2 * math.pi

class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
	def area(self):
		return self.width * self.height

class Shape:
	def __init__(self):
		pass
	def area(self):
		return 0

class Square(Shape):
	def __init__(self, side):
		self.val = side
	def area(self):
		return self.val**2

if __name__ == '__main__':
	#Ex41
	#print(*filtereven((1,2,3,4,5,6,7,8,9)), sep=', ')

	#Ex42
	#print(*squaresof((1,2,3,4,5,6,7,8,9)), sep=', ')

	#Ex43
	#print(*squaresofeven((1,2,3,4,5,6,7,8,9)), sep=', ')

	#Ex44
	#print(*filterevennum(20), sep=', ')

	#Ex45
	#print(*mapsquares(range(1,21)), sep=', ')

	#Ex46
	#jack = American()
	#jack.printNationality()

	#Ex47
	#raj = NewYorker()
	#raj.printNationality()

	#Ex48
	#circle = Circle(5)
	#print('{0:.2f}'.format(circle.area()))

	#Ex49
	#rectangle = Rectangle(8, 12)
	#print(rectangle.area())

	#Ex50
	#square = Square(4)
	#print(square.area())
