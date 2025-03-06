import re
import secrets
import string
import time

def validate_parameters(length, nums, special_chars, uppercase, lowercase):
    """Valida os parâmetros de entrada para garantir que sejam válidos."""
    if length < (nums + special_chars + uppercase + lowercase):
        raise ValueError("O comprimento da senha deve ser maior ou igual à soma dos requisitos mínimos.")

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """Gera uma senha segura e personalizável."""
    # Define os caracteres possíveis para a senha
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    # Combina todos os caracteres
    all_characters = letters + digits + symbols

    # Valida os parâmetros de entrada
    validate_parameters(length, nums, special_chars, uppercase, lowercase)

    while True:
        password = ''
        # Gera a senha
        for _ in range(length):
            password += secrets.choice(all_characters)
        
        constraints = [
            (nums, r'\d'),
            (special_chars, fr'[{symbols}]'),
            (uppercase, r'[A-Z]'),
            (lowercase, r'[a-z]')
        ]

        # Verifica se a senha atende aos critérios
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
    return password

def main():
    try:
        while True:
            # Gera uma nova senha a cada 5 segundos (personalize conforme necessário)
            new_password = generate_password()
            print('Generated password:', new_password)
            time.sleep(5)  # Ajuste o intervalo (em segundos) conforme necessário
    except KeyboardInterrupt:
        print("\nPassword generation stopped.")

if __name__ == '__main__':
    main()
