import string
import unittest

from password.new_password import generate_password

class TestPassword(unittest.TestCase):

    def test_password_characters(self):
        """Тест, что при генерации используются только допустимые символы"""
        valid_characters = string.ascii_letters + string.digits + string.punctuation
        password = generate_password(100)  # Генерируем длинный пароль для более надежной проверки
        for char in password:
            self.assertIn(char, valid_characters)

    def test_length(self):
        """Тест, что при генерации используются только допустимые символы"""
        password = generate_password(10)  # Генерируем длинный пароль для более надежной проверки
        self.assertGreater(len(password), 19)

"""
Допиши еще один тест из предложенных. Или придумай свой.
Если сможешь написать больше, то будет круто!

Тест, что длина пароля соответствует заданной
Тест, что два сгенерированных подряд пароля различаются
"""
