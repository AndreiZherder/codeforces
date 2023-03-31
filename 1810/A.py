import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    for i, num in enumerate(a, start=1):
        if num <= i:
            print('YES')
            return
    print('NO')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
