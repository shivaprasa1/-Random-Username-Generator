import random

class UsernameGenerator:
    def __init__(self):
        self.adjectives = self._load_words("data/adjectives.txt")
        self.nouns = self._load_words("data/nouns.txt")
        self.special_chars = self._load_words("data/special_chars.txt")

    def _load_words(self, file_path):
        """Load words from a text file."""
        with open(file_path, 'r') as file:
            words = file.read().strip().split(', ')
        return words

    def generate(
        self,
        include_numbers=False,
        include_special_chars=False,
        min_length=6,
        max_length=12
    ):
        """Generate a random username."""
        adjective = random.choice(self.adjectives)
        noun = random.choice(self.nouns)
        username = adjective + noun

        if include_numbers:
            username += str(random.randint(0, 999))

        if include_special_chars:
            username += random.choice(self.special_chars)

        # Ensure length constraints
        if len(username) < min_length:
            username += str(random.randint(10 ** (min_length - len(username) - 1), 10 ** (min_length - len(username)) - 1))
        if len(username) > max_length:
            username = username[:max_length]

        return username