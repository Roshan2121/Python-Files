#objects as arguements to user defined functions.

class Fruits:

	def __init__(self, cost = 200, quantity = '2kg'):
		self.cost = cost
		self.quantity = quantity

	def setValue(self, cost, quantity):
		self.cost = cost
		self.quantity = quantity

apple = Fruits(100, )
orange = Fruits(70, '2kg')

def Print(object):
	print('cost = ', object.cost)
	print('quantity = ', object.quantity)

Print(apple)
Print(orange)