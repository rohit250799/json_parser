from lexer import display_tokens_in_terminal
from accept_file import extract_token_for_parser, actual_filename



print(f'The tokens are: {extract_token_for_parser(actual_filename=actual_filename)}')