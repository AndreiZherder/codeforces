import sys
from itertools import chain


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)



def input_interactive(*args):
    print(' '.join(chain('?', map(str, args))))
    sys.stdout.flush()
    return int(input())


def print_interactive(*args):
    print(' '.join(chain('!', map(str, args))))
    sys.stdout.flush()


def solution():
    n, m = [int(num) for num in input().split()]
    x = input_interactive(1, 1)
    if x >= n:
        y = input_interactive(1, x + 1)
        print_interactive(y + 1, x + 1)
    elif x >= m:
        y = input_interactive(x + 1, 1)
        print_interactive(x + 1, y + 1)
    else:
        y = input_interactive(1, x + 1)
        z = input_interactive(x + 1, 1)
        if x == y == z:
            print_interactive(x + 1, x + 1)
        elif y == x:
            print_interactive(x + 1, z + 1)
        else:
            print_interactive(y + 1, x + 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
