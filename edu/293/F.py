from collections import Counter
from os import path
from sys import stdin, stdout


filename = '../../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    s = input()
    t = Counter(input())
    cur = Counter()
    j = 0
    ans = 0
    for i in range(n):
        cur[s[i]] += 1
        while any(cur[c] > t[c] for c in cur):
            cur[s[j]] -= 1
            if cur[s[j]] == 0:
                del cur[s[j]]
            j += 1
        ans += i - j + 1
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
