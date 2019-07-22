#Sorting lists of objects.

class Fruits:

	def __init__(self, name, cost):
		self.name = name
		self.cost = cost

	def priority(self):      #used to tell the sorted method to sort by cost.
		return self.cost

	def __str__(self):
		return self.name

Apple = Fruits('Apple', 300)
Orange = Fruits('Orange', 140)
Lemon = Fruits('Lemon', 100)
Grapes = Fruits('Grapes', 120)

instances = list([Apple, Orange, Lemon, Grapes])

sorted_list = sorted(instances, key=Fruits.priority)

for fruit in sorted_list:
	print(fruit)

