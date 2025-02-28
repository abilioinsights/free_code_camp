## Password Generator
This project is a customizable password generator written in Python. It generates secure passwords by randomly selecting characters from a combination of letters, digits, and special symbols. The generator ensures that the generated passwords meet certain customizable criteria, such as containing at least one digit, one uppercase letter, one lowercase letter, and one special character. Additionally, the generator can run automatically at specified intervals to continuously produce new passwords until manually stopped.

## Features
- Customizable Password Generation: Specify the length, and minimum required digits, special characters, uppercase, and lowercase letters.
- Automatic Mode: Continuously generate passwords at custom intervals until stopped.
- Secure Randomness: Uses the secrets module for cryptographic-grade randomness.

## Requirements
- Python 3.x
 
## Usage
### Running the Password Generator
<p>Manual Mode: You can generate a password manually by calling the generate_password() function with or without parameters.</p>
  
```py
  python password_generator.py
```
<p>The default password length is 16 characters, with at least one digit, one special character, one uppercase letter, and one lowercase letter.</p>

<p>Automatic Mode: To automatically generate passwords at regular intervals, use the continuous mode with customizable timing:</p>

```py
python password_generator.py --auto --interval 5
```

This will generate a new password every 5 seconds. You can stop the process anytime by pressing ``Ctrl+C``.

## Customization Options
<p>You can customize the password generation with the following options:</p>

```py
generate_password(length = 16, nums = 1, special_chars = 1, uppercase = 1, lowercase = 1)
```


- ``length``: Total length of the password (default: 16).
- ``nums``: Minimum number of digits (default: 1).
- ``special_chars``: Minimum number of special characters (default: 1).
- ``uppercase``: Minimum number of uppercase letters (default: 1).
- `` lowercase``: Minimum number of lowercase letters (default: 1).

## Example

```py
new_password = generate_password(length=12, nums=2, special_chars=2, uppercase=2, lowercase=2)
print('Generated password:', new_password)
```

## Continuous Mode Example

```py
python password_generator.py --auto --interval 10
```

This will generate a password every 10 seconds until you stop the script.

## How It Works
- ``Character Pool``: The generator combines all possible characters from digits, lowercase and uppercase letters, and special symbols.
- ``Constraints``: The password must meet specific constraints for digits, special characters, and letter cases. These constraints are enforced using regular expressions.
- ``Automatic Mode``: In continuous mode, the generator keeps creating new passwords at specified intervals and displays them in the console.

## License
This project is licensed under the MIT License.
