import sys

def fill_html_content():
	content = """
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<title>A simple HTML document</title>
		</head>
		<body>
   			<p>Hello World!<p>
			<table>
  			<tr>
  				<th>Company</th>
  				<th>Contact</th>
  				<th>Country</th>
  			</tr>
  			<tr>
  				<td>Alfreds Futterkiste</td>
  				<td>Maria Anders</td>
  				<td>Germany</td>
  			</tr>
  			<tr>
  				<td>Centro comercial Moctezuma</td>
  				<td>Francisco Chang</td>
  				<td>Mexico</td>
  			</tr>
</table> 
		</body>
		</html>
	"""
	return content

def periodic_table():
	html_content = fill_html_content()

	with open("periodic_table.html", "w") as html_file:
		html_file.write(html_content)

if __name__ == "__main__":
	periodic_table()