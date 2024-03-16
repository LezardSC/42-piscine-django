class Intern():
	def __init__(self, string=None):
		if string is None:
			self.Name = "My name? I'm nobody, an intern, I have no name."
		else:
			self.Name = string
	def __str__(self):
		return self.Name

class Coffee():
	def __str__(self):
		return "This is the worst coffee you ever tasted."
	def work():


def name_intern():
	intern1 = Intern()
	intern2 = Intern("Mark")

	print(intern1)
	print(intern2)

if __name__ == "__main__":
	name_intern()