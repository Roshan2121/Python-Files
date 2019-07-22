
class Fruits:

	def __init__(self, name, cost):
		self.name = name
		self.cost = cost

	def Print(self):
		print(self.name)

Apple = Fruits('Apple', 300)
Orange = Fruits('Orange', 140)

key = Fruits.Print
key(Apple)     #This works however Apple.key() does not, which says that the key is not the method of this class.
