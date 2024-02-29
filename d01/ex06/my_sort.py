import sys

def my_sort():
	d = {
		'Hendrix': '1942',
		'Allman': '1946',
		'King': '1925',
		'Clapton': '1945',
		'Johnson': '1911',
		'Berry': '1926',
		'Vaughan': '1954',
		'Cooder': '1947',
		'Page': '1944',
		'Richards': '1943',
		'Hammett': '1962',
		'Cobain': '1967',
		'Garcia': '1942',
		'Beck': '1944',
		'Santana': '1947',
		'Ramone': '1948',
		'White': '1975',
		'Frusciante': '1970',
		'Thompson': '1949',
		'Burton': '1939',
	}

	dict(sorted(d.items()))
	for last_name, birth_year in d.items():
		print(f"{birth_year} : {last_name}")
	dict(sorted(d.items(), key=lambda item: item[1]))
	for last_name, birth_year in d.items():
		print(f"{birth_year} : {last_name}")

if __name__ == "__main__":
	my_sort()