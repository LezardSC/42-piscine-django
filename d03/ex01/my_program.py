from local_lib import path

def test_path():
	dir = path.Path('new_dir')
	dir.mkdir()
	dir.cd()
	file = path.Path('new_file')
	file.touch()
	file.write_text("Hello World")
	text = file.read_text()
	print(text)

if __name__ == "__main__":
	test_path()