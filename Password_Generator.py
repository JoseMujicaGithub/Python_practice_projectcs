import re
import secrets
import string


def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):

    # Define the possible characters for the password
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combine all characters
    all_characters = letters + digits + symbols

    while True:
        password = ''
        # Generate password
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password

def validate_input_num(input_description=": "): 
    while True:
        try:
            num=int(input(input_description))
        except:
            print('===Invalid Input===')
            continue
        if type(num)==int:
            break
    return num

print('===This program generates a password===\n')

while True:
    length=validate_input_num('Enter the legth\n: ')
    if length>=5:
        break
    else:
        print('==Password must be 5 characters atleast==')

nums=validate_input_num('Enter an amount of numeric characters\n: ')
special_chars=validate_input_num('Enter an amount of special characters\n: ')
uppercase=validate_input_num('Enter an amount of uppercase characters\n: ')
lowercase=validate_input_num('Enter an amount of lowercase characters\n: ')

if __name__ == '__main__':
    new_password = generate_password(length, nums, special_chars, uppercase, lowercase)
    print('Generated password:', new_password)