def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]

    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

custom_key = 'happycoding'

while True:
    # Allow the user to edit the custom key
    change_key = input("\nDo you want to change the encryption key? (yes/no): ").lower()
    
    if change_key == 'yes':
        custom_key = input("Enter the new custom key: ")
        print(f"Custom key updated to: {custom_key}")
    
    # Request user input for text to decrypt
    text = input("\nEnter the text to decrypt (or type 'exit' to quit): ")
    
    # Check if the user wants to leave
    if text.lower() == 'exit':
        print("Exiting the program.")
        break
    
    decryption = decrypt(text, custom_key)
    print(f'\nDecrypted text: {decryption}\n')
