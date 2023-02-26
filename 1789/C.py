import sys
from collections import Counter

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n,m = (int(num) for num in input().split())
    a = input().split()
    d = Counter({num: m + 1 for num in a})
    for i in range(m):
        index, v = input().split()
        index = int(index)
        d[a[index - 1]] -= (m - i)
        d[v] += (m - i)
        a[index - 1] = v
    ans = 0
    for v in d.values():
        ans += (2 * m - v + 1) * v // 2
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
