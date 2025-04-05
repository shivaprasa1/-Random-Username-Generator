class FileHandler:
    @staticmethod
    def save_usernames(usernames, file_path="data/saved_usernames.txt"):
        """Save generated usernames to a file."""
        with open(file_path, 'a') as file:
            for username in usernames:
                file.write(f"{username}\n")

    @staticmethod
    def load_usernames(file_path="data/saved_usernames.txt"):
        """Load previously generated usernames."""
        try:
            with open(file_path, 'r') as file:
                return [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            return []