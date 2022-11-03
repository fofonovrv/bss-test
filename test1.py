# Нельзя использовать метод json(), тогда просто форматируем как текст
def read_json_file() -> None:
	try:
		json_file = open('task3.json')
		json_file
		num_of_tab = 0
		for line in json_file:
			line = line.replace('"', '').replace('[', '').replace(']', '').replace('\n', '')[4:]
			if (not "{" in line) and \
			(not "}" in line) and \
			(line.replace(' ', '') != ''):
				line = line.replace('    ', '\t')
				line = line[:-1] if line[-1] == ',' else line
				if len(line) > 1:
					print(line)
	except Exception as ex:
		print(f"Ошибка: {ex}")


if __name__ == "__main__":
	read_json_file()