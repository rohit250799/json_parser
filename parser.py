from lexer import display_tokens_in_terminal
from accept_file import extract_token_for_parser, actual_filename

generated_string_for_parsing = extract_token_for_parser(actual_filename=actual_filename)

class My_Stack_for_JSON_validation:
    def __init__(self):
        self.val = []
    def push_token(self, token) -> None:
        self.val.append(token)
    def pop_token(self):
        return self.val.pop(-1)
    def peek(self):
        return self.val[0]
    def is_empty(self) -> bool:
        return False if self.val else True
class Parser:
    def __init__(self, generated_string_for_parsing):
        self.tokens = generated_string_for_parsing
        my_stack = My_Stack_for_JSON_validation()

    def is_Object(self, my_stack) -> bool:
        if not self.tokens: return f'Incorrect tokens provided'
        else:
            for object_token in self.tokens:
                if object_token == '{':
                    my_stack.push_token()

    def evaluation(self, generated_string_for_parsing):
            

# print(f'The tokens are: {extract_token_for_parser(actual_filename=actual_filename)}')
print(f'The tokens are: {generated_string_for_parsing}')
