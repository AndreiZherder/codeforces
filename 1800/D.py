import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    s = input() + '#'
    ans = n - 1
    cnt = 1
    for i in range(1, n + 1):
        if s[i] == s[i - 1]:
            cnt += 1
        else:
            if cnt >= 3:
                ans -= (cnt - 2)
            cnt = 1
    for i in range(2, n + 1):
        if s[i] != s[i - 1] and s[i] == s[i - 2]:
            ans -= 1
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
