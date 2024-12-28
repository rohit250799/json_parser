import argparse
import tokenize

parser = argparse.ArgumentParser(prog='file_acceptance', description='accept name of file')
parser.add_argument('filename', help='add filename for validity checking')
filename_supplied_as_argument = parser.parse_args()

    

    
actual_filename = filename_supplied_as_argument.filename
print(actual_filename)

def total_char_length_in_file(actual_filename) -> int:
    with open(actual_filename) as f:
        file_content = f.read()
        total_char_length = len(file_content)
    return total_char_length

def generating_tokens_from_file(actual_filename):
    with tokenize.open(actual_filename) as f:
        tokens = tokenize.generate_tokens(f.readline)
        for token in tokens:
            print(token)

def extract_token_for_parser(actual_filename) -> str:
    token_list = []
    file_content = open(actual_filename, 'r')
    if file_content: return file_content.read()
    return f'The tokens could not be generated unfortunately'
