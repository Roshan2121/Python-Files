
#Creating a class.
class Fruits:

	#This function is like a constructor in C++.
	def __init__(self, quantity): 
		self.quantity = quantity   #creates an instance called quantity and assigns value to it.

	def instanceGenerator(self):
		self.y = 10000

	def quantity_taken(self):
		print('Quantity = ', self.quantity) #prints the value of the instance quantity.
	
	def cost_print(self):
		print('Cost = ', self.cost)  #prints the value of the cost instance.

#defining objects.
Apple  = Fruits('4kg')
Orange = Fruits('10kg')

#Creates an instance of the object called cost and assign value to it.
Apple.cost = 20
Orange.cost = 12

Apple.cost_print()       #calls the method.
Orange.cost_print()      #calls the method.

Apple.quantity_taken()
Orange.quantity_taken()

Apple.instanceGenerator()
print(Apple.y)
#Hence we saw how to use objects, instances and functions. We can create inctances inside any method in the class or outside the class by initialization method as shown above.
