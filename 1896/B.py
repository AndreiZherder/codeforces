from collections import deque
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
    n = int(input())
    s = list(input())
    indexes = deque()
    ans = 0
    for i in range(n - 1):
        if s[i] == 'A' and s[i + 1] == 'B':
            indexes.append(i)
    seen = set(indexes)
    while indexes:
        ans += 1
        i = indexes.popleft()
        s[i] = 'B'
        s[i + 1] = 'A'
        if i - 1 >= 0:
            if s[i - 1] == 'A' and i - 1 not in seen:
                seen.add(i - 1)
                indexes.append(i - 1)
        if i + 2 < n:
            if s[i + 2] == 'B' and i + 1 not in seen:
                seen.add(i + 1)
                indexes.append(i + 1)
    print(ans)


def main():
    t = int(input())
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
