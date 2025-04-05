class UsernameValidator:
    @staticmethod
    def is_valid(username, existing_usernames=None):
        """Check if a username is valid."""
        if existing_usernames and username in existing_usernames:
            return False
        return 3 <= len(username) <= 20  # Example length constraints