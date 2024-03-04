import sys

def fill_css_content():
	content = "td{ border: 1px solid black; }"
	return content

def fill_table_rows(elements):
	table_rows = []

	for element in elements:
		element_data = element.split(", ")
		position_data = element_data[0].split('=')[1].strip().split(':')
		table_row = f"""
			<tr>
				<td>{element_data[0].split('=')[0].strip()}</td>
				<td>{position_data[1].strip()}</td>
				<td>{element_data[1].split(':')[1].strip()}</td>
				<td>{element_data[2].split(':')[1].strip()}</td>
				<td>{element_data[3].split(':')[1].strip()}</td>
				<td>{element_data[4].split(':')[1].strip()}</td>
			</tr>
		"""
		table_rows.append(table_row)

	return table_rows

def fill_html_content(elements):
	table_rows = fill_table_rows(elements)

	content = f"""
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<title>Periodic Table</title>
			<link rel="stylesheet" type="text/css" href="periodic_table.css">
		</head>
		<body>
   			<h1><b>Periodic Table</b></h1>
			<table>
				<tr>
					<th>Element</th>
					<th>Position</th>
					<th>Number</th>
					<th>Symbol</th>
					<th>Molar Mass</th>
					<th>Electron Configuration</th>
				</tr>
				{''.join(table_rows)}
  				
			</table> 
		</body>
	</html>
	"""
	return content

def periodic_table():
	with open("periodic_table.txt", "r") as elements_file:
		elements = [line.strip() for line in elements_file]

	html_content = fill_html_content(elements)
	css_content = fill_css_content()

	with open("periodic_table.html", "w") as html_file:
		html_file.write(html_content)
	with open("periodic_table.css", "w") as css_file:
		css_file.write(css_content)

if __name__ == "__main__":
	periodic_table()