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

def replace_key_words(content, dict):
	pattern = re.compile(r'\{(\w+)\}')

	def replace(match):
		key = match.group(1)
		return str(dict.get(key, f'{{{key}}}'))

	return pattern.sub(replace, content)

def render():
	if len(sys.argv) != 2:
		print("Error\nThe program takes one argument.")
		return
	template = sys.argv[1]
	if not os.path.exists(template):
		print(f"Error\nFile \'{template}\' does not exist.")
		return
	if not template.endswith(".template"):
		print("Error\nFile must end with \'.template\'.")
		return

	dict_settings = create_dic_settings('settings.py')
	
	with open(template, 'r') as source:
		content = source.read()

	rendered_content = replace_key_words(content, dict_settings)
	filename = os.path.splitext(os.path.basename(template))[0]
	html_filename = f"{filename}.html"

	with open(html_filename, 'w') as dest:
		dest.write(rendered_content)

if __name__ == "__main__":
	render()