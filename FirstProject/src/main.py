from generator import UsernameGenerator
from file_handler import FileHandler
from validator import UsernameValidator

def main():
    generator = UsernameGenerator()
    file_handler = FileHandler()
    validator = UsernameValidator()

    print("\n=== Random Username Generator ===")
    
    # Get user preferences
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special chars? (y/n): ").lower() == 'y'
    num_usernames = int(input("How many usernames to generate? "))
    
    # Generate usernames
    usernames = []
    existing_usernames = file_handler.load_usernames()
    
    for _ in range(num_usernames):
        while True:
            username = generator.generate(include_numbers, include_special_chars)
            if validator.is_valid(username, existing_usernames):
                usernames.append(username)
                break
    
    print("\nGenerated Usernames:")
    for username in usernames:
        print(f"- {username}")
    
    # Save to file
    if input("\nSave usernames? (y/n): ").lower() == 'y':
        file_handler.save_usernames(usernames)
        print("Usernames saved!")

if __name__ == "__main__":
    main()