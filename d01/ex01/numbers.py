def numbers():
	with open("numbers.txt", "r") as openFile:
		content = openFile.read()
	processedContent = content.replace(",", "\n")
	print(processedContent)

if __name__ == '__main__':
	numbers()