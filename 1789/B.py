import sys
from math import gcd

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def dec_to_bin(x: int, n: int) -> str:
    return bin(x)[2:].zfill(n)


def solution():
    n = int(input())
    s = input()

    left = 0
    right = n - 1
    inv = False
    while left < right:
        if not inv:
            if s[left] != s[right]:
                inv = True
        else:
            if s[left] == s[right]:
                if s[left:right + 1] != s[right:left - 1: -1]:
                    print('NO')
                    return
                else:
                    print('YES')
                    return
        left += 1
        right -= 1
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
