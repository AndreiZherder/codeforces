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
    n, k = [int(num) for num in input().split()]
    a = [int(num) for num in input().split()]
    a.sort(key=lambda x: 10 - x % 10)
    i = 0
    while i < n and k:
        x = min(k, (10 - a[i] % 10) % 10)
        a[i] += x
        k -= x
        i += 1
    ans = 0
    for ai in a:
        ans += ai // 10
    if k:
        y = sum(100 - ai for ai in a)
        ans += min(y // 10, k // 10)
    print(ans)


def main():
    t = 1
    while t:
        solution()
        t -= 1


if __name__ == '__main__':
    main()
