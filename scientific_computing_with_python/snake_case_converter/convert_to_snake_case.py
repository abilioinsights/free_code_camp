def convert_to_snake_case(pascal_or_camel_cased_string):

    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in pascal_or_camel_cased_string
    ]

    return ''.join(snake_cased_char_list).strip('_')

def convert_words_to_snake_case(sentence):
    words = sentence.split()  # Split the sentence into words
    snake_case_words = [convert_to_snake_case(word) for word in words]  # Convert each word
    return '_'.join(snake_case_words)  # Join the converted words with "_"

def main():
    # Example with multiple PascalCase or camelCase words
    sentence = input("Enter a sentence in PascalCase or camelCase: ")
    print(convert_words_to_snake_case(sentence))

main()
