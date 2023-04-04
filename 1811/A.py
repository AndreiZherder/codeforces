import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n, d = [int(num) for num in input().split()]
    s = input()
    for i in range(n):
        if int(s[i]) < d:
            print(f'{s[:i]}{d}{s[i:]}')
            return
    print(f'{s}{d}')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
