import sys

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    s = input()
    c = min(s)
    for i in range(n - 1, -1, -1):
        if s[i] == c:
            break
    print(s[i] + s[:i] + s[i + 1:])


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
