# ДЗ 01_02_1
def rle_encode(data: str) -> str:
	# Инициализация переменных
	encoded_string = ""
	count = 1

	# Перебор символов строки, начиная со второго символа
	for i in range(1, len(data)):
		if data[i] == data[i - 1]:
			count += 1
		else:
			# Добавляем результат для предыдущего символа
			encoded_string += f"{count}{data[i - 1]}"
			count = 1
	# Добавляем результат для последнего символа
	encoded_string += f"{count}{data[-1]}"
	return encoded_string

# Пример входной строки
# WWWWWWWWWWWWBWWWWWWWWWWWWBBB
# aaaabbcccccccddddgggggggggggg
input_str = "WWWWWWWWWWWWBWWWWWWWWWWWWBBB"

# Кодируем строку
encoded_str = rle_encode(input_str)

# Выводим результат
print(encoded_str)  # Output: 4a2b7c4d12g