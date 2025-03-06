def convert_to_snake_case(pascal_or_camel_cased_string):
    """Converts a PascalCase or camelCase string to snake_case."""
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]
    return ''.join(snake_cased_char_list).strip('_')

def split_sentence_into_words(sentence):
    """Splits a sentence into words."""
    return sentence.split()

def convert_words_to_snake_case(sentence):
    """Converts each word in a sentence to snake_case and joins them with underscores."""
    words = split_sentence_into_words(sentence)
    snake_case_words = [convert_to_snake_case(word) for word in words]
    return '_'.join(snake_case_words)

def main():
    """Main function to handle user input and output."""
    try:
        sentence = input("Enter a sentence in PascalCase or camelCase: ").strip()
        if not sentence:
            raise ValueError("Input cannot be empty.")
        
        snake_case_sentence = convert_words_to_snake_case
