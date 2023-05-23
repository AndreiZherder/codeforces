import sys


def input():
    return sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    a = []
    for i in range(n):
        a.append(input().split())
        a[-1][0] = int(a[-1][0])
    min_both = 10 ** 20
    min_first = 10 ** 20
    min_second = 10 ** 20
    for time, s in a:
        if s == '11':
            min_both = min(min_both, time)
        if s[0] == '1':
            min_first = min(min_first, time)
        if s[1] == '1':
            min_second = min(min_second, time)
    ans = min(min_both, min_first + min_second)
    if ans == 10 ** 20:
        print(-1)
    else:
        print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
