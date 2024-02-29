import sys

def find_counterpart(item: str):
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

	name = ""
	item_cap = item.title()
	if item_cap in states:
		name = states.get(item_cap)
		capital_city = capital_cities.get(name)
		print(f"{capital_city} is the capital of {item_cap}")
	elif item_cap in capital_cities.values():
		for abbr in capital_cities:
			if item_cap == capital_cities[abbr]:
				name = abbr
		for state in states:
			if name == states[state]:
				print(f"{item_cap} is the capital of {state}")
	else:
		print(f"{item} is neither a capital city nor a state")

def all_in():
	if len(sys.argv) == 2:
		input_list = sys.argv[1].split(',')
		for item in input_list:
			item = item.strip()
			if (len(item) > 0):
				find_counterpart(item)

if __name__ == "__main__":
	all_in()