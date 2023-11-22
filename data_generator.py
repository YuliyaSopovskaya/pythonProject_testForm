import random
import string

def generate_random_string(length): # генерирует случайную строку заданной длины
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_email():  # генерирует случайное электронное письмо
    username = generate_random_string(8) # создание имени пользователя
    return f"{username}@example.com"
