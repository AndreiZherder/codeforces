from os import path
from sys import stdin, stdout


filename = '../templates/input.txt'
if path.exists(filename):
    stdin = open(filename, 'r')


def input():
    return stdin.readline().rstrip()


def print(*args, sep=' ', end='\n'):
    stdout.write(sep.join(map(str, args)))
    stdout.write(end)


def solution():
    n, m = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    b = [int(num) for num in input().split()]
    ans = 0
    i = 0
    cur = 0
    prev = 10 ** 20
    for j in range(m):
        if b[j] == prev:
            ans += cur
            continue
        cur = 0
        while i < n and a[i] < b[j]:
            i += 1
        while i < n and a[i] == b[j]:
            i += 1
            cur += 1
        ans += cur
        prev = b[j]
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
