This project implements the Vigenère Cipher, a classic encryption algorithm used for both encrypting and decrypting text based on a repeating keyword. The cipher shifts each letter in the message according to the corresponding letter in the key, offering a simple yet effective method of cryptography.

The main features of this project include:

Encryption and Decryption Functions:
The encrypt function encodes a given message using a specified key.
The decrypt function decodes the message using the same key, reversing the encryption process.
Dynamic Key Input:
Users are prompted to input a new custom key for encryption/decryption, allowing flexibility in the encryption process.
Support for Non-Letter Characters:
Any non-letter characters (spaces, punctuation, numbers) in the message are preserved in their original positions, maintaining the format of the input text.
Interactive Loop:
The program runs in an interactive mode, continuously prompting the user for input text and offering the option to modify the encryption key until the user chooses to exit.
How It Works:
The Vigenère Cipher uses a keyword to determine the shift applied to each letter in the message. The key is repeated or truncated to match the length of the message.
Each letter in the message is shifted by the number of positions defined by the corresponding letter in the key. For decryption, the reverse operation is applied.
The cipher operates on lowercase English letters, while non-alphabetical characters are left unchanged in the final message.
Example:
Given the text:

nginx
Copiar
Editar
mrttaqrhknsw ih puggrur
With the key:

nginx
Copiar
Editar
happycoding
The program decrypts it back to:

nginx
Copiar
Editar
hello zaira
Usage:
Run the program, enter the text you'd like to encrypt or decrypt, and input a custom encryption key when prompted. You can change the key at any time during execution, allowing multiple encryptions and decryptions with different keys in one session.

This project demonstrates a basic understanding of string manipulation, loops, and conditional logic in Python, while showcasing the classic cryptographic technique of the Vigenère cipher.