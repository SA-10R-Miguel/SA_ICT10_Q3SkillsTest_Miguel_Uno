# Skills Test 3rd Quarter
from pyscript import display, document


def username_verification(e):
    document.getElementById('output').innerHTML = ' '

    username = document.getElementById('username').value
    username_length = len(username)
    # Checks if username is fit for the criteria
    if username_length < 10:
        display(f'Your username is too short. Add at least {10 - username_length} more character/s to proceed.', target='output')
    else:
        return(True)


def password_verification(e):
    document.getElementById('output').innerHTML = ' '

    password = document.getElementById('password').value
    password_length = len(password)
    password_has_number = any(char.isdigit() for char in password)
    password_has_letter = any(char.isalpha() for char in password)
    # Checks if password is also fit for the criteria using if-elif-else statements
    if password_length < 10:
        display(f'Your password is too short. Add at least {10 - password_length} more character/s to proceed.', target='output')
    elif not password_has_letter:
        display(f'Password must contain at least one letter.', target='output')
    elif not password_has_number:
        display(f'Password must contain at least one number.', target='output')
    else:
        return(True)


def account_creation(e):
    document.getElementById('output').innerHTML = ' '

    if username_verification(e) == True and password_verification(e) == True:
        display(f'Account created. You may now log in using your credentials.', target='output')
    else:
        display(f'Try again. Follow the rules next time LMAO', target='output')