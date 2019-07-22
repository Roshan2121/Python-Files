
class Fruits:

	count = 0     #Class instance.

	def __init__(self, cost, quantity):
		self.cost = cost
		self.quantity = quantity

	def __str__(self):
		Fruits.count += 1
		return 'Fruit' + str(Fruits.count)

	def __add__(self, object):    #self is apple and object is orange.
		holder = Fruits(0, 0)
		holder.cost = self.cost + object.cost
		holder.quantity = self.quantity + object.quantity
		return holder

apple = Fruits(100, '1kg')
orange = Fruits(140, '2kg')

print(apple)
print(orange)
lemon = apple + orange #calls apple.add(orange)
print(lemon.cost)    #Prints 100+140=240.

#__sub__() 