# ДЗ 01_2
def rle_encode(input_string: str) -> str:
	# Инициализация переменных
	encoded_string = ""
	count = 1

	# Перебор символов строки, начиная со второго символа
	for i in range(1, len(input_string)):
		if input_string[i] == input_string[i - 1]:
			count += 1
		else:
			# Добавляем результат для предыдущего символа
			encoded_string += f"{count}{input_string[i - 1]}"
			count = 1
	# Добавляем результат для последнего символа
	encoded_string += f"{count}{input_string[-1]}"
	return encoded_string

# Пример входной строки
input_str = "aaaabbcccccccddddgggggggggggg"

# Кодируем строку
encoded_str = rle_encode(input_str)

# Выводим результат
print(encoded_str)  # Output: 4a2b7c4d12g