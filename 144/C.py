from collections import Counter
from os import path
from sys import stdin, stdout


filename = "../templates/input.txt"
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    def good(cur: Counter) -> bool:
        total = 0
        for c in p:
            if cur[c] > p[c]:
                return False
            total += p[c] - cur[c]
        return total == cur['?']

    s = input()
    n = len(s)
    p = input()
    k = len(p)
    p = Counter(p)
    ans = 0
    cur = Counter(s[:k])
    if good(cur):
        ans += 1
    for i in range(k, n):
        cur[s[i]] += 1
        cur[s[i - k]] -= 1
        ans += good(cur)
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
