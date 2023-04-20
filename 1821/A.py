import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    s = input()
    if s[0] == '0':
        print(0)
        return
    cnt = s[1:].count('?')
    ans = 10 ** cnt
    if s[0] == '?':
        ans *= 9
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
