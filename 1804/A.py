import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    a, b = [int(num) for num in input().split()]
    a, b = abs(a), abs(b)
    if a == b:
        print(2 * a)
        return
    if b < a:
        a, b = b, a
    print(a + a + 1 + 2 * (b - a - 1))


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
