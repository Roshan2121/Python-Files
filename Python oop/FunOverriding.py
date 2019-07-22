
class Fruits:

	def __init__(self, name):
		self.name = name

	def Print(self):
		print(self.name)

class Apple(Fruits):

	def __init__(self, name, cost, color):
		Fruits.__init__(self, name)
		self.cost = cost
		self.color = color

	def Print(self):
		print(self.color, self.cost)

apple = Apple('Apple', 200, 'Red')
apple.Print()  #calls the Print method of the class Apple.
Fruits.Print(apple) #calls the Print method of the class Fruits.

#Hence to invoke the parent class methods we have to expilcitly mention it.
