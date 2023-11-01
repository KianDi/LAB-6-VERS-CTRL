
# my name is Kian Disuanco
def encode_password(password):
    # Check if the input password is a string of 8 digits
    if not password.isdigit() or len(password) != 8:
        return "Invalid password format"

    # Initialize an empty string to store the encoded password
    encoded_password = ""

    # Iterate through each digit in the input password
    for digit in password:
        # Shift each digit up by 3 numbers and wrap around if needed
        encoded_digit = str((int(digit) + 3) % 10)
        encoded_password += encoded_digit

    return encoded_password

def decode_password(password):
    result = ''
    for i in range(0, len(password)):
        result += str((int(password[i])-3)%10)
    return result


def display_menu():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        user_input = ''
        user_input = input("Please enter an option: ")
        if user_input == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode_password(password)
            print("Your password has been encoded and stored!")
        elif user_input == "2":
            print("The encoded password is", encoded_password + ", and the original password is", password)
        elif user_input == "3":
            break


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    display_menu()


