import sys


class Redirection(object):
    def __init__(self, in_obj, out_obj):
        self.input = in_obj
        self.output = out_obj

    def read_line(self):
        res = self.input.readline()
        self.output.write(res)
        return res


if __name__ == '__main__':
    if not sys.stdin.isatty():
        sys.stdin = Redirection(in_obj=sys.stdin, out_obj=sys.stdout)

    a = input('enter some string: ')
    b = input('enter another string: ')
    print('entered strings are: ', repr(a), 'and', repr(b))
