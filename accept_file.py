import argparse

#class TestParser:
    

parser = argparse.ArgumentParser(prog='file_acceptance', description='accept name of file')
parser.add_argument('filename', help='add filename for validity checking')

filename_supplied = parser.parse_args()

print(filename_supplied.filename)

