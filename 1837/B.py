import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    s = input()
    best = 0
    cur = 0
    symb = '<'
    for c in s:
        if c == symb:
            cur += 1
        else:
            symb = c
            cur = 1
        best = max(best, cur)
    print(best + 1)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
