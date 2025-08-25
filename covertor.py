def decimal_to_binary(n):
    return bin(n)[2:]

def decimal_to_octal(n):
    return oct(n)[2:]

def decimal_to_hex(n):
    return hex(n)[2:].upper()

def binary_to_decimal(b):
    return int(b, 2)

def binary_to_octal(b):
    return oct(int(b, 2))[2:]

def binary_to_hex(b):
    return hex(int(b, 2))[2:].upper()

def octal_to_decimal(o):
    return int(o, 8)

def octal_to_binary(o):
    return bin(int(o, 8))[2:]

def octal_to_hex(o):
    return hex(int(o, 8))[2:].upper()

def hex_to_decimal(h):
    return int(h, 16)

def hex_to_binary(h):
    return bin(int(h, 16))[2:]

def hex_to_octal(h):
    return oct(int(h, 16))[2:]

def main():
    options = {
        1: ("Decimal to Binary", decimal_to_binary),
        2: ("Decimal to Octal", decimal_to_octal),
        3: ("Decimal to Hexadecimal", decimal_to_hex),
        4: ("Binary to Decimal", binary_to_decimal),
        5: ("Binary to Octal", binary_to_octal),
        6: ("Binary to Hexadecimal", binary_to_hex),
        7: ("Octal to Decimal", octal_to_decimal),
        8: ("Octal to Binary", octal_to_binary),
        9: ("Octal to Hexadecimal", octal_to_hex),
        10: ("Hexadecimal to Decimal", hex_to_decimal),
        11: ("Hexadecimal to Binary", hex_to_binary),
        12: ("Hexadecimal to Octal", hex_to_octal),
    }

    while True:
        print("\n--- Number System Converter ---")
        print("0. Exit")
        for key in sorted(options):
            print(f"{key}. {options[key][0]}")

        choice = input("\nEnter your choice (number): ").strip()
        if choice == "0":
            print("Exiting...")
            break

        # Validate input choice as integer
        try:
            choice_num = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number from the menu.")
            continue

        if choice_num not in options:
            print("Invalid choice. Please select a valid option from the menu.")
            continue

        label, func = options[choice_num]

        # Input prompt and validation
        if "Decimal to" in label:
            user_input = input(f"Enter a decimal number for '{label}': ").strip()
            try:
                value = int(user_input)
            except ValueError:
                print("Invalid decimal number. Try again.")
                continue
        elif "Binary to" in label:
            user_input = input(f"Enter a binary number (0s and 1s) for '{label}': ").strip()
            if not all(c in "01" for c in user_input):
                print("Invalid binary number. Try again.")
                continue
            value = user_input
        elif "Octal to" in label:
            user_input = input(f"Enter an octal number (digits 0-7) for '{label}': ").strip()
            if not all(c in "01234567" for c in user_input):
                print("Invalid octal number. Try again.")
                continue
            value = user_input
        elif "Hexadecimal to" in label:
            user_input = input(f"Enter a hexadecimal number (0-9, A-F) for '{label}': ").strip().upper()
            if not all(c in "0123456789ABCDEF" for c in user_input):
                print("Invalid hexadecimal number. Try again.")
                continue
            value = user_input
        else:
            value = input(f"Enter input value for '{label}': ").strip()

        try:
            result = func(value)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}. Invalid input for this conversion.")

if __name__ == "__main__":
    main()
