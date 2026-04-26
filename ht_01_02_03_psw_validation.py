def validate_password(password: str) -> dict[str, bool]:
    # Проверка длины пароля
    length_check = len(password) >= 8

    # Проверка наличия заглавных и строчных букв
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    case_check = has_upper and has_lower

    # Проверка наличия цифр
    digits_check = any(char.isdigit() for char in password)

    # Проверка наличия спецсимволов
    special_symbols = "!@#$%^&*()-_+="
    special_check = any(char in special_symbols for char in password)

    # Общий результат
    is_strong = length_check and case_check and digits_check and special_check

    # Возвращаем словарь с результатами
    return {
        "length": length_check,
        "case": case_check,
        "digits": digits_check,
        "special": special_check,
        "is_strong": is_strong
    }

# password = "StrongPass1!"
# password = "weak"
# password = "NoSpecialChar123"
password = "Qwerty123!"
print(validate_password(password))
# Output:
# {
#     'length': True,
#     'case': True,
#     'digits': True,
#     'special': True,
#     'is_strong': True
# }