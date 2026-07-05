import random

# Character sets
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()"

# User inputs
length = int(input("Enter password length: "))

upper_choice = input("Include uppercase letters? (Y/N): ").upper()
lower_choice = input("Include lowercase letters? (Y/N): ").upper()
number_choice = input("Include numbers? (Y/N): ").upper()
symbol_choice = input("Include special characters? (Y/N): ").upper()

# Build the character pool
character_pool = ""

if upper_choice == "Y":
    character_pool += uppercase

if lower_choice == "Y":
    character_pool += lowercase

if number_choice == "Y":
    character_pool += numbers

if symbol_choice == "Y":
    character_pool += symbols

# Check if the pool is empty
if character_pool == "":
    print("You must select at least one type of character.")
else:
    password = ""

    for i in range(length):
        password += random.choice(character_pool)

    print("Generated Password:", password)
