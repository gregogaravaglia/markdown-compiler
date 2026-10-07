#!/usr/bin/python3

'''Convert a Markdown document into an HTML file.'''

from markdown_compiler import convert_file


def main():
    # process command line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True)
    parser.add_argument('--add_css', action='store_true')
    args = parser.parse_args()

    # call the main function
    convert_file(args.input_file, args.add_css)


if __name__ == '__main__':
    main()
