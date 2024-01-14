# main.py
import argparse
import sys
from lexer import lexer
from c_parser import parser
from translator import process_program
from preprocess import pre_process
from preprocess import add_main

def main():
    # Create the parser
    arg_parser = argparse.ArgumentParser(description='Parse C code to python.')
    arg_parser.add_argument('-s', '--source', type=str, help='Path to the C source file')
    arg_parser.add_argument('-o', '--output', type=str, help='Path to the output python file')
    args = arg_parser.parse_args()
    if args.source:
        try:
            with open(args.source, 'r',encoding='utf-8') as file:
                data = file.read()
        except FileNotFoundError:
            print(f"Error: File {args.source} not found.")
            sys.exit(1)
    data=pre_process(data)
    lexer.input(data)
    result = parser.parse(data)
    output=process_program(result)
    output=add_main(output)
    if args.output:
        try:
            with open(args.output, 'w') as file:
                file.write(output)
        except FileNotFoundError:
            print(f"Error: File {args.output} not found.")
            sys.exit(1)
    if output:
        print(output)
        with open("output.py", 'w') as file:
                file.write(output)
    
if __name__ == '__main__':
    main()
