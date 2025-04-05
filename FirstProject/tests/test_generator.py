import unittest
from src.generator import UsernameGenerator

class TestUsernameGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = UsernameGenerator()

    def test_generate_basic(self):
        username = self.generator.generate()
        self.assertTrue(len(username) >= 6)

    def test_generate_with_numbers(self):
        username = self.generator.generate(include_numbers=True)
        self.assertTrue(any(c.isdigit() for c in username))

if __name__ == "__main__":
    unittest.main()