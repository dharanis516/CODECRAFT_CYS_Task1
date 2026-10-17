def shift_text(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            # 'A' is 65 and 'a' is 97 in ASCII, so pick the right starting point
            start = ord("A") if char.isupper() else ord("a")

            # 1. Convert the letter to a number from 0 to 25
            # 2. Add the shift and use % 26 to wrap around the alphabet
            # 3. Convert the number back to a letter
            new_position = (ord(char) - start + shift) % 26
            result += chr(start + new_position)
        else:
            result += char

    return result


def encrypt(message, shift):
    """Encrypt a message by shifting letters forward."""
    return shift_text(message, shift)


def decrypt(message, shift):
    """Decrypt a message by shifting letters backward."""
    return shift_text(message, -shift)


def get_shift():
    """Keep asking until the user enters a valid whole number."""
    while True:
        try:
            return int(input("Enter the shift value (e.g. 3): "))
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("=== Caesar Cipher ===")

    while True:
        print("\n1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            message = input("Enter the message to encrypt: ")
            shift = get_shift()
            print("Encrypted message:", encrypt(message, shift))
        elif choice == "2":
            message = input("Enter the message to decrypt: ")
            shift = get_shift()
            print("Decrypted message:", decrypt(message, shift))
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")


if __name__ == "__main__":
    main()