
class Fruits:

	count = 0     #Class instance.

	def __init__(self, cost, quantity):
		self.cost = cost
		self.quantity = quantity

	def __str__(self):
		Fruits.count += 1
		return 'Fruit' + str(Fruits.count)

apple = Fruits(100, '1kg')
orange = Fruits(140, '2kg')

print(apple)
print(orange)