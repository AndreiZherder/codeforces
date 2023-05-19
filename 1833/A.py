import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    s = input()
    seen = set()
    ans = 0
    for i in range(n - 1):
        if s[i:i + 2] not in seen:
            ans += 1
            seen.add(s[i:i + 2])
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
