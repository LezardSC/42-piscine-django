import random
from beverages import HotBeverage, Coffee, Tea, Chocolate, Cappuccino

class CoffeeMachine:
	def __init__(self):
		self.usage = 0
	
	class EmptyCup(HotBeverage):
		def __init__(self):
			self.name = "empty cup"
			self.price = 0.90
		
		def description(self):
			return "An empty cup?! Gimme my money back!"
	
	class BrokenMachineException(Exception):
		def __init__(self):
			Exception.__init__(self, "This coffee machine has to be repaired.")
	
	def repair(self):
		self.usage = 0

	def serve(self, drink):
		give_beverage = random.random()

		if self.usage < 10:
			self.usage += 1
			if give_beverage < 0.5:
				return drink
			else:
				return CoffeeMachine.EmptyCup()
		else:
			raise CoffeeMachine.BrokenMachineException

def coffeeMachine():
	machine = CoffeeMachine()
	coffee = Coffee()
	tea = Tea()
	chocolate = Chocolate()
	cappuccino = Cappuccino()

	for i in range(23):
		try:
			cup = machine.serve(coffee)
			print(cup)
		except Exception as e:
			print(e)
	machine.repair()
	for i in range(11):
		try:
			cup = machine.serve(tea)
			print(cup)
		except Exception as e:
			print(e)
	print(chocolate)

if __name__ == "__main__":
	coffeeMachine()