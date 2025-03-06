def vigenere_cipher(message, key, direction=1):
    """
    Applies the Vigenère cipher to encrypt or decrypt a message.

    Args:
        message (str): The message to be processed.
        key (str): The encryption/decryption key.
        direction (int): 1 for encryption, -1 for decryption.

    Returns:
        str: The processed message.
    """
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message:
        # Append non-alphabetic characters as-is
        if not char.isalpha():
            final_message += char
        else:
            # Find the corresponding key character
            key_char = key[key_index % len(key)].lower()
            key_index += 1

            # Calculate the offset and new character index
            offset = alphabet.index(key_char)
            index = alphabet.find(char.lower())
            new_index = (index + offset * direction) % len(alphabet)

            # Preserve the original case
            if char.isupper():
                final_message += alphabet[new_index].upper()
            else:
                final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    """
    Encrypts a message using the Vigenère cipher.

    Args:
        message (str): The message to encrypt.
        key (str): The encryption key.

    Returns:
        str: The encrypted message.
    """
    return vigenere_cipher(message, key, direction=1)

def decrypt(message, key):
    """
    Decrypts a message using the Vigenère cipher.

    Args:
        message (str): The encrypted message.
        key (str): The decryption key.

    Returns:
        str: The decrypted message.
    """
    return vigenere_cipher(message, key, direction=-1)

def get_valid_key():
    """
    Prompts the user to enter a valid key (alphabetic characters only).

    Returns:
        str: The valid key provided by the user.
    """
    while True:
        key = input("Enter the custom key (letters only): ").strip()
        if key.isalpha():
            return key
        print("Invalid key. Please use only letters.")

def main():
    """
    Main function to handle user interaction.
    """
    custom_key = 'happycoding'

    while True:
        # Allow the user to change the encryption key
        change_key = input("\nDo you want to change the encryption key? (yes/no): ").lower()
        
        if change_key == 'yes':
            custom_key = get_valid_key()
            print(f"Custom key updated to: {custom_key}")
        
        # Request user input for text to decrypt
        text = input("\nEnter the text to decrypt (or type 'exit' to quit): ")
        
        # Exit the program if the user types 'exit'
        if text.lower() == 'exit':
            print("Exiting the program.")
            break
        
        # Decrypt the message and display the result
        decrypted_text = decrypt(text, custom_key)
        print(f'\nDecrypted text: {decrypted_text}\n')

if __name__ == "__main__":
    main()
