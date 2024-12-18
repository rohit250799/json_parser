import argparse

parser = argparse.ArgumentParser(prog='file_acceptance', description='accept name of file')
parser.add_argument('filename', help='add filename for validity checking')
filename_supplied_as_argument = parser.parse_args()

    

    
actual_filename = filename_supplied_as_argument.filename
print(actual_filename)

