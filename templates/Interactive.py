import sys
from itertools import chain


def input_interactive(*args):
    print(' '.join(chain('?', map(str, args))))
    sys.stdout.flush()
    return input()


def print_interactive(*args):
    print(' '.join(chain('!', map(str, args))))
    sys.stdout.flush()