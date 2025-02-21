import random

def luhn_generate_check_digit(partial_card_number):
    """Calculates the correct check digit for a valid card number."""
    digits = [int(d) for d in partial_card_number]
    sum_of_odd_digits = sum(digits[-1::-2])
    sum_of_even_digits = sum((d * 2 if d * 2 < 10 else d * 2 - 9) for d in digits[-2::-2])
    total = sum_of_odd_digits + sum_of_even_digits
    check_digit = (10 - (total % 10)) % 10
    return str(check_digit)

def generate_card_number(card_type):
    """Generates a valid card number for a specific card brand."""
    card_prefixes = {
        "Visa": ["4"],
        "MasterCard": [str(i) for i in range(51, 56)] + [str(i) for i in range(2221, 2721)],
        "American Express": ["34", "37"],
        "Diners Club": ["300", "301", "302", "303", "304", "305", "36", "38"],
        "Discover": ["6011", "65"] + [str(i) for i in range(622126, 622926)] + [str(i) for i in range(644, 650)],
        "JCB": ["35"]
    }
    
    if card_type not in card_prefixes:
        return None

    prefix = random.choice(card_prefixes[card_type])
    length = 16 if card_type not in ["American Express", "Diners Club"] else 15

    random_digits = ''.join(str(random.randint(0, 9)) for _ in range(length - len(prefix) - 1))
    partial_card_number = prefix + random_digits
    check_digit = luhn_generate_check_digit(partial_card_number)
    
    full_card_number = partial_card_number + check_digit

    # Checks if the generated number is valid before returning
    if verify_card_number(full_card_number):
        return full_card_number
    else:
        return generate_card_number(card_type)  # Tries to generate again if invalid

def verify_card_number(card_number):
    """Checks if a card number is valid using the Luhn algorithm."""
    sum_of_odd_digits = sum(int(digit) for digit in card_number[-1::-2])
    
    sum_of_even_digits = 0
    for digit in card_number[-2::-2]:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def get_card_type(card_number):
    """Detects the card brand based on the first digits."""
    if card_number.startswith('4') and len(card_number) in [13, 16]:
        return "Visa"
    elif any(card_number.startswith(str(i)) for i in range(51, 56)) or any(card_number.startswith(str(i)) for i in range(2221, 2721)):
        return "MasterCard"
    elif card_number.startswith(('34', '37')) and len(card_number) == 15:
        return "American Express"
    elif card_number.startswith(('300', '301', '302', '303', '304', '305', '36', '38')) and len(card_number) == 14:
        return "Diners Club"
    elif card_number.startswith(('6011', '65')) or any(card_number.startswith(str(i)) for i in range(622126, 622926)) or any(card_number.startswith(str(i)) for i in range(644, 650)):
        return "Discover"
    elif card_number.startswith('35') and len(card_number) == 16:
        return "JCB"
    else:
        return "Unknown"

def main():
    while True:
        print("\nChoose an option:")
        print("1. Validate a card number")
        print("2. Generate a valid card number")
        print("3. Exit")

        option = input("Enter your choice (1-3): ").strip()

        if option == "1":
            card_number = input("Enter the card number (or 'back' to return): ").strip()
            if card_number.lower() == 'back':
                continue

            card_translation = str.maketrans({'-': '', ' ': ''})
            translated_card_number = card_number.translate(card_translation)

            if not translated_card_number.isdigit():
                print("Invalid number! Enter only digits, spaces, or hyphens.")
                continue

            card_type = get_card_type(translated_card_number)
            is_valid = verify_card_number(translated_card_number)

            print(f"Card Type: {card_type}")
            print("Status: VALID!" if is_valid else "Status: INVALID!")

        elif option == "2":
            print("\nChoose a card brand to generate:")
            print("1. Visa\n2. MasterCard\n3. American Express\n4. Diners Club\n5. Discover\n6. JCB\n7. Back")

            choice = input("Enter your choice (1-7): ").strip()
            card_types = ["Visa", "MasterCard", "American Express", "Diners Club", "Discover", "JCB"]

            if choice == "7":
                continue
            elif choice in map(str, range(1, 7)):
                card_type = card_types[int(choice) - 1]
                generated_card = generate_card_number(card_type)
                print(f"Generated Card ({card_type}): {generated_card}")
            else:
                print("Invalid option. Try again.")

        elif option == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
