"""
write a function that asks for user input with the input() function
Ask them to create a password that is greater than >6 and <12 characters long ( 6< pwd < 12)

Use an assert statement to validate their password choice

"""

def get_password() -> str:
    pwd = input("Enter a password (6-12 characters): ")
    assert 6 < len(pwd) < 12, "Password must be greater than 6 and less than 12 characters long."
    return pwd

if __name__ == "__main__":
    try:
        password = get_password()
        print("Password accepted:", password)
    except AssertionError as e:
        print("Error:", e)