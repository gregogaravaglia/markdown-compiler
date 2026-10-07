#!/usr/bin/python3

'''Convert a Markdown document into an HTML file.'''

from markdown_compiler import *

def main():
    # process command line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    # FIXME:
    # to get the command_lines test to pass,
    # you will need to uncomment the line below;
    # then add the args.add_css variable as a parameter to convert_file
    #parser.add_argument('--add_css', action='store_true')
    args = parser.parse_args()

    # call the main function
    convert_file(args.input_file, False)

if __name__ == '__main__':
    main()
