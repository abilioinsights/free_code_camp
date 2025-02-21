# Generates valid credit card numbers for testing.
This was the original code learned in class, I decided to improve it a little, since I learned about Luhn's algorithm, I optimized it with some extra resources.
```py
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

main()
```


## Installation

Ensure you have **Python 3.x** installed on your system.

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/card-validator.git
   ```
2. Navigate to the project folder:
   ```sh
   cd card-validator
   ```
3. Run the script:
   ```sh
   python card_validator.py
   ```

## Usage

After running the script, the user will be prompted to choose an option:

```
Choose an option:
1. Validate a card number
2. Generate a valid card number
3. Exit
Enter your choice (1-3):
```

### Validate a Card Number

- Enter a credit card number (spaces and dashes are allowed but will be removed automatically).
- The program will determine if the card number is valid and display its provider.

### Generate a Valid Card Number

- Choose a card provider from the menu.
- The program will generate and display a valid credit card number for testing.

### Exit

- Simply choose option `3` to exit the program.

## Example

```
Choose an option:
1. Validate a card number
2. Generate a valid card number
3. Exit
Enter your choice (1-3): 2

Choose a card type to generate:
1. Visa
2. MasterCard
3. American Express
4. Diners Club
5. Discover
6. JCB
7. Back
Enter your choice (1-7): 1

Generated Card (Visa): 4539352456524328
```

## License

This project is licensed under the MIT License.

## Contributing

Feel free to fork this repository, create a feature branch, and submit a pull request!

## Contact

For any issues or suggestions, open an issue on the GitHub repository.

