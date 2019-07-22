
class Fruits:

	def __init__(self, name, cost):
		self.name = name
		self.cost = cost

	def Print(self):
		print(self.name)

Apple = Fruits('Apple', 300)
Orange = Fruits('Orange', 140)

key = Fruits.Print   #This is same like (key = lambda x : x.Print()) where x is Apple or Orange.
key(Apple)     #This works however Apple.key() does not, which says that the key is not the method of this class.
