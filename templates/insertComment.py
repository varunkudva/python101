#!/usr/bin/python
import sys
import os

TEMPLATE_FILE = 'template.py'

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


if __name__ == '__main__':
    arg = sys.argv[1]
    if os.path.isdir(arg):
        for file in os.listdir(arg):
            if '.py' in file:
                # only in python files
                insert_comment(os.path.join(arg, file))
    elif os.path.isfile(arg):
        if '.py' in arg:
            # only in python files
            insert_comment(arg)
    else:
        print("invalid input {}".format(sys.argv[1]))

