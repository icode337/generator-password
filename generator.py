import random
import string

letters = tuple(string.ascii_letters)
numbers = tuple(string.digits)
symbols = tuple(string.punctuation)

print("Генератор паролей")
length_password = int(input("Введите сколько чисел требуется для пароля\n"))
nr_letters = int(input("Введите сколько букв требуется для пароля\n"))
length_password = length_password - nr_letters
print(f"для создания пароля требуется {length_password} значений")
nr_symbols = int(input("Введите сколько спецсимволов требуется для пароля\n"))
length_password = length_password - nr_symbols
print(f"для создания пароля требуется {length_password} значений")
nr_numbers = int(input("Введите сколько чисел требуется для пароля\n"))

password_list = []

for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

print(random.shuffle(password_list))

password = ""
for char in password_list:
    password += char

print(f"пароль сгенерирован\n{password}")