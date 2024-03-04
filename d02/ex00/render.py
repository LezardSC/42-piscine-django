import sys
import os
import re

def create_dic_settings(file_path):
	result_dict = {}

	with open(file_path, 'r') as file:
		for line in file:
			key, value = map(str.strip, line.split('='))
			result_dict[key] = eval(value)
	return result_dict

def replace_keys_for_values(content, dict):
	

def render():
	if len(sys.argv) != 2:
		print("temp error args")
		return
	dict_settings = create_dic_settings('settings.py')
	
	with open('myCV.template', 'r') as source:
		content = source.read()

	with open('myCV.html', 'w') as dest:
		dest.write(content)

if __name__ == "__main__":
	render()