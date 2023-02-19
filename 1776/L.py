import sys
from collections import Counter
from math import gcd

input = lambda: sys.stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)))
    sys.stdout.write(end)


def solution():
    n = int(input())
    s = input()
    q = int(input())
    queries = []
    for i in range(q):
        queries.append([int(num) for num in input().split()])
    ans = []
    cnt = Counter(s)
    z = max(cnt.values())
    w = n - z
    for a, b in queries:
        divisor = gcd(a, b)
        a //= divisor
        b //= divisor
        if a > b:
            a, b = b, a
        if a == b:
            if z == w:
                ans.append('YES')
            else:
                ans.append('NO')
        elif (z - w) % (b - a) != 0:
            ans.append('NO')
        else:
            k = (z - w) // (b - a)
            if a * k <= w:
                ans.append('YES')
            else:
                ans.append('NO')

    print('\n'.join(ans))


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
