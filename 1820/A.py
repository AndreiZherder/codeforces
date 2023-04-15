import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    s = input()
    if s == '^':
        print(1)
        return
    ans = 0
    if s[0] == '_':
        ans += 1
    if s[-1] == '_':
        ans += 1
    for i in range(1, len(s)):
        if s[i] == '_' and s[i - 1] == '_':
            ans += 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
