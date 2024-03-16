class Intern():
	class Coffee():
		def __str__(self):
			return "This is the worst coffee you ever tasted."

	def __init__(self, string=None):
		if string is None:
			self.Name = "My name? I'm nobody, an intern, I have no name."
		else:
			self.Name = string

	def __str__(self):
		return self.Name


	def work(self):
		raise Exception("I'm justs an intern, I can't do that...")

	def make_coffee(self):
		return Intern.Coffee()

def name_intern():
	intern1 = Intern()
	intern2 = Intern("Mark")

	print(intern1)
	print(intern2)
	try:
		intern1.work()
	except Exception as e:
		print(e)
	print(intern2.make_coffee())

if __name__ == "__main__":
	name_intern()
