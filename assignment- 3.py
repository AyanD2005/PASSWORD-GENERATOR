
import random
import string

def generate_password(length=12):
    # Define characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate password using random.choice
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    # Default password length is 12 characters
    password_length = 12
    try:
        password_length = int(input("Enter desired password length (default is 12): "))
    except ValueError:
        print("Invalid input. Using default password length.")

    if password_length <= 0:
        print("Password length should be greater than 0. Using default password length.")
        password_length = 12

    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)

