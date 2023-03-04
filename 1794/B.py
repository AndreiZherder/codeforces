import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = [int(num) for num in input().split()]
    if n == 1:
        print(*a)
        return
    for i in range(1, n):
        if a[i - 1] == 1:
            a[i - 1] += 1
            if i - 2 >= 0 and a[i - 1] % a[i - 2] == 0:
                a[i - 1] += 1
        while a[i] % a[i - 1] == 0:
            a[i] += 1
    print(*a)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
