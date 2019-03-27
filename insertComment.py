#!/usr/bin/python
import sys
import os
import argparse

TEMPLATE_FILE = 'templates/template.py'

def insert_comment(src_file):
    text = ''
    comment_str = ''

    # read comment string from template
    with open(TEMPLATE_FILE) as fd:
        comment_str = fd.read()

    with open(src_file) as fd:
        if fd.readline().startswith('"""'):
            # comment exists already
            return
        else:
            fd.seek(0)
            line = fd.readline()
            if line.startswith('#!'):
                # let shebang start the file
                comment_str = line + comment_str
                text = fd.read()
            else:
                fd.seek(0)
                text = fd.read()

    with open(src_file, 'w') as fd:
        if text.startswith('\n\n'):
            fd.write(comment_str + text)
        elif text.startswith('\n'):
            fd.write(comment_str + '\n' + text)
        else:
            fd.write(comment_str + '\n\n' + text)
        print("Updated {}".format(src_file))


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory")
    args = parser.parse_args()
    if args.directory:
        print args.directory
    else:
        print args
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory")
    parser.add_argument("filename", nargs='?', default=None, help = "file to add comment")
    args = parser.parse_args()
    if args.directory:
        if os.path.isdir(args.directory):
            for file in os.listdir(args.directory):
                if '.py' in file:
                    # only in python files
                    insert_comment(os.path.join(args.directory, file))
        else:
            print "Invalid input: {} is not a directory".format(args.directory)
    else:
        if os.path.isfile(args.filename):
            if '.py' in args.filename:
                # only in python files
                insert_comment(args.filename)
        else:
            print("invalid input {}".format(sys.argv[1]))

    sys.exit(0)

