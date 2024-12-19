
from accept_file import actual_filename, generating_tokens_from_file, total_char_length_in_file

char_length_in_file = total_char_length_in_file(actual_filename)
print(f'The length of characters is: {char_length_in_file}')

#def display_tokens_in_terminal()
display_tokens_in_terminal = generating_tokens_from_file(actual_filename)