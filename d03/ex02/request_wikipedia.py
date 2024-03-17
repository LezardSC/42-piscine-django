import requests
import json
import sys
import dewiki

def wiki_scrap():
	if len(sys.argv) != 2:
		return print("Error\nNeed one parameter")
	param = sys.argv[1]
	session = requests.Session()
	api = 'https://fr.wikipedia.org/w/api.php'
	params = {
        "action": "parse",
		"page": param,
		"prop": "wikitext",
        "format": "json",
		"redirects": True,
		"formatversion": 2
    }
	
	request = session.get(api, params=params)
	data = request.json()
	result = dewiki.from_string(data["parse"]["wikitext"])

	file = open(param + ".wiki", "w")
	file.write(result)
	file.close()


if __name__ == "__main__":
	wiki_scrap()
