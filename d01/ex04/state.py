import sys

def state():
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}

	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}

	if len(sys.argv) == 2:
		capital = sys.argv[1]
		name = ""
		if capital in capital_cities.values():
			for abbr in capital_cities:
				if capital == capital_cities[abbr]:
					name = abbr
			for state in states:
				if name == states[state]:
					print(state)
		else:
			print("Unknown capital city")

if __name__ == "__main__":
	state()