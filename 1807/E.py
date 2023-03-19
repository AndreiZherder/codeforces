import sys
from itertools import chain


input = lambda: sys.stdin.readline().rstrip()


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
    n = int(input())
    a = [int(num) for num in input().split()]
    left = 0
    right = n - 1
    while left < right:
        mid = left + (right - left) // 2
        lst = [mid - left + 1] + list(range(left + 1, mid + 1 + 1))
        x = input_interactive(*lst)
        if x > sum(a[left:mid + 1]):
            right = mid
        else:
            left = mid + 1
    print_interactive(left + 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
