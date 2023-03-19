import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    if n == 1:
        if a[0] == 1:
            print('YES')
            return
        else:
            print('NO')
            return
    a.sort()
    total = 1
    for num in a[1:]:
        if num > total:
            print('NO')
            return
        total += num
    print('YES')


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
